#!/usr/bin/env python3
"""V20 bounded acquisition of supplemental official datasets.

All downloaded objects are retained byte-for-byte with URL, timestamp, size and SHA256.
ACS API extracts are supplemental query snapshots and never replace the 28 frozen originals.
"""
from __future__ import annotations
import csv, gzip, hashlib, io, json, os, pathlib, time, urllib.error, urllib.parse, urllib.request, zipfile
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "raw_external" / "v20"
QA = ROOT / "qa_v20" / "data_sources"
UA = "Y-CITY-SYORA-V20-research/1.0 (source provenance; contact via repository)"
CITIES = {
    "06": ["66000"], "08": ["20000"], "13": ["04000"], "17": ["14000"],
    "25": ["07000"], "27": ["43000"], "37": ["55000"], "41": ["59000"],
    "42": ["61000"], "48": ["05000"], "53": ["63000"], "55": ["48000"],
}
ACS_TABLES = {
    "B15003": ["001E","001M","002E","002M","022E","022M","023E","023M","024E","024M","025E","025M"],
    "B23025": ["001E","001M","002E","002M","004E","004M","005E","005M","007E","007M"],
    "B25003": ["001E","001M","002E","002M","003E","003M"],
    "B25064": ["001E","001M"],
    "B25077": ["001E","001M"],
    "B08201": ["001E","001M","002E","002M"],
}
SOURCES = [
    ("IMLS_PLS_FY2024_OUTLET_ZIP","https://www.imls.gov/sites/default/files/2026-06/pls_fy2024_csv.zip","www.imls.gov","imls_fy2024_csv.zip","zip"),
    ("NCES_EDGE_PUBLIC_SCHOOLS_2425","https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_PUBLICSCH_2425.zip","nces.ed.gov","EDGE_GEOCODE_PUBLICSCH_2425.zip","zip"),
    ("NCES_POSTSECONDARY_SCHOOLS_2425_CSV","https://data-nces.opendata.arcgis.com/api/download/v1/items/c09067e617894cbca0798c53967c795b/csv?layers=0","data-nces.opendata.arcgis.com","postsecondary_school_locations_2425.csv","csv"),
    ("EPA_AIRDATA_ANNUAL_MONITOR_2024","https://aqs.epa.gov/aqsweb/airdata/annual_conc_by_monitor_2024.zip","aqs.epa.gov","annual_conc_by_monitor_2024.zip","zip"),
    ("NOAA_GHCN_STATIONS","https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt","www.ncei.noaa.gov","ghcnd-stations.txt","text"),
    ("NOAA_GHCN_DAILY_2024","https://www.ncei.noaa.gov/pub/data/ghcn/daily/by_year/2024.csv.gz","www.ncei.noaa.gov","2024.csv.gz","gzip"),
    ("COMAP_SUMMARY_ORIGINAL","https://www.contest.comap.com/highschool/contests/himcm/flyers/HiMCM-MidMCM_Summary.tex","www.contest.comap.com","HiMCM-MidMCM_Summary_ORIGINAL.tex","tex"),
]

def utc():
    return datetime.now(timezone.utc).isoformat()

def sha_file(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest()

def allowed(url, host):
    u=urllib.parse.urlparse(url)
    if u.scheme!="https" or u.hostname!=host: raise ValueError("HOST_OR_SCHEME_NOT_ALLOWLISTED")

def request_bytes(url, host, limit=1024*1024*1024, attempts=2, timeout=90):
    allowed(url,host); errors=[]
    for attempt in range(attempts):
        try:
            req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept-Encoding":"identity"})
            with urllib.request.urlopen(req,timeout=timeout) as r:
                allowed(r.geturl(),host)
                if r.status!=200: raise ValueError("EXPECTED_HTTP_200")
                length=r.headers.get("Content-Length")
                if length and int(length)>limit: raise ValueError("BYTE_BUDGET_EXCEEDED")
                chunks=[]; n=0; h=hashlib.sha256()
                while True:
                    b=r.read(1024*1024)
                    if not b: break
                    n+=len(b)
                    if n>limit: raise ValueError("BYTE_BUDGET_EXCEEDED")
                    h.update(b); chunks.append(b)
                if length and n!=int(length): raise ValueError("CONTENT_LENGTH_MISMATCH")
                return b"".join(chunks), {"http_status":r.status,"response_url":r.geturl(),"content_type":r.headers.get("Content-Type"),"last_modified":r.headers.get("Last-Modified"),"etag":r.headers.get("ETag"),"bytes":n,"sha256":h.hexdigest()}
        except Exception as e:
            errors.append(f"{type(e).__name__}: {e}")
            if isinstance(e,urllib.error.HTTPError) and e.code in (401,403,404,429): break
            if attempt+1<attempts: time.sleep(2**attempt)
    raise RuntimeError("DOWNLOAD_FAILED: "+" | ".join(errors))

def validate(p, kind):
    if kind=="zip":
        if not zipfile.is_zipfile(p): raise ValueError("NOT_ZIP")
        with zipfile.ZipFile(p) as z:
            if z.testzip() is not None: raise ValueError("ZIP_CRC_FAILURE")
            names=z.namelist()
            if not names: raise ValueError("EMPTY_ZIP")
            return {"schema":"ZIP_CRC_PASS","members":len(names),"sample_members":names[:8]}
    if kind=="csv":
        with p.open(encoding="utf-8-sig",newline="") as f:
            rd=csv.reader(f); header=next(rd)
            if len(header)<3: raise ValueError("CSV_HEADER_TOO_SHORT")
            return {"schema":"CSV_HEADER_PASS","columns":len(header),"header":header[:30]}
    if kind=="gzip":
        with gzip.open(p,"rb") as f: sample=f.read(4096)
        if not sample: raise ValueError("EMPTY_GZIP_PAYLOAD")
        return {"schema":"GZIP_STREAM_PASS","sample_bytes":len(sample)}
    if kind=="text":
        with p.open(encoding="ascii",errors="strict") as f: first=f.readline()
        if len(first.strip())<20: raise ValueError("TEXT_RECORD_INVALID")
        return {"schema":"ASCII_TEXT_PASS","first_record":first.rstrip()[:120]}
    if kind=="tex":
        s=p.read_text(encoding="utf-8-sig")
        if not all(x in s for x in (r"\\documentclass",r"\\begin{document}",r"\\end{document}")): raise ValueError("TEX_TEMPLATE_INVALID")
        return {"schema":"TEX_STRUCTURE_PASS"}
    raise ValueError("UNKNOWN_VALIDATOR")

def fetch_source(sid,url,host,name,kind):
    dest=OUT/"files"/name; dest.parent.mkdir(parents=True,exist_ok=True)
    receipt=QA/"receipts"/(sid+".json"); receipt.parent.mkdir(parents=True,exist_ok=True)
    if dest.exists() and receipt.exists():
        old=json.loads(receipt.read_text())
        if old.get("sha256")==sha_file(dest):
            return old | {"status":"REUSED_HASH_VERIFIED"}
    record={"source_id":sid,"publisher_host":host,"url":url,"retrieved_utc":utc(),"status":"FAILED","release_eligible":False}
    try:
        b,meta=request_bytes(url,host)
        tmp=dest.with_suffix(dest.suffix+".part");tmp.write_bytes(b)
        semantic=validate(tmp,kind);tmp.replace(dest)
        record.update(meta,status="DOWNLOADED_ORIGINAL_WITH_SHA",path=str(dest.relative_to(ROOT)),semantic_qa=semantic,
                      origin_verification="DIRECT_TLS_SOURCE",release_eligible=False,
                      interpretation="Supplementary source; not silently added to frozen M1")
    except Exception as e:
        record["error"]=repr(e)
    receipt.write_text(json.dumps(record,ensure_ascii=False,indent=2)+"\n")
    return record

def acs_api_snapshots():
    records=[];base="https://api.census.gov/data/2024/acs/acs5"
    dest=OUT/"acs_api";dest.mkdir(parents=True,exist_ok=True)
    for table,suffixes in ACS_TABLES.items():
        variables=[f"{table}_{x}" for x in suffixes]
        fields="NAME,"+",".join(variables)
        for state,places in CITIES.items():
            for geography in ("tract","place"):
                query={"get":fields,"for":f"{geography}:*","in":f"state:{state}"}
                url=base+"?"+urllib.parse.urlencode(query)
                try:
                    payload,meta=request_bytes(url,"api.census.gov",limit=128*1024*1024,attempts=2,timeout=60)
                    obj=json.loads(payload)
                    if not isinstance(obj,list) or len(obj)<2 or "NAME" not in obj[0]: raise ValueError("ACS_API_RESPONSE_SCHEMA_INVALID")
                    if geography=="place":
                        # Keep all place rows in each target state; exact frozen GEOIDs are selected downstream.
                        wanted=set(places)
                        obj=[obj[0]]+[row for row in obj[1:] if row[-1] in wanted]
                    rel=pathlib.Path("acs_api")/table/f"state_{state}_{geography}.json"
                    path=dest/table/f"state_{state}_{geography}.json";path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(payload)
                    records.append({"source_id":f"ACS_API_{table}_{state}_{geography}","url":url,"retrieved_utc":utc(),"path":str((OUT/rel).relative_to(ROOT)),
                                    "bytes":meta["bytes"],"sha256":meta["sha256"],"rows":len(obj)-1,"status":"DOWNLOADED_QUERY_SNAPSHOT",
                                    "origin_verification":"DIRECT_TLS_SOURCE","not_a_replacement_for_original_dat":True})
                except Exception as e:
                    records.append({"source_id":f"ACS_API_{table}_{state}_{geography}","url":url,"retrieved_utc":utc(),"status":"FAILED","error":repr(e)})
                time.sleep(0.25)
    return records

def main():
    QA.mkdir(parents=True,exist_ok=True);OUT.mkdir(parents=True,exist_ok=True)
    records=[]
    for src in SOURCES:
        records.append(fetch_source(*src))
        print(records[-1]["source_id"],records[-1]["status"],flush=True)
    api=acs_api_snapshots()
    report={"version":"V20","checked_utc":utc(),"optional_sources":records,"acs_api_snapshots":api,
            "meaning":"Only records with DOWNLOADED status are byte-acquired. API query snapshots supplement but do not replace required whole-table originals. None of these optional records changes frozen M1 weights."}
    (QA/"V20_OPTIONAL_SOURCE_ACQUISITION.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    return 0 if any(x.get("status")=="DOWNLOADED_ORIGINAL_WITH_SHA" for x in records) or any(x.get("status")=="DOWNLOADED_QUERY_SNAPSHOT" for x in api) else 3

if __name__=="__main__": raise SystemExit(main())
