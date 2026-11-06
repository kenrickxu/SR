#!/usr/bin/env python3
"""Generate reviewed owner-hosted direct rules; never publish or schedule by itself."""
import argparse,hashlib,json,re,urllib.request
from pathlib import Path
REPO="Loyalsoldier/clash-rules"
def fetch(url):
    return urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"Ken-SR-rule-maintenance"}),timeout=45).read()
def convert(body):
    lines=body.decode("utf-8-sig").splitlines()
    if not lines or lines[0].strip()!="payload:": raise ValueError("unexpected upstream format")
    rows=[];seen=set()
    for line in lines[1:]:
        if not line.strip() or line.lstrip().startswith("#"):continue
        m=re.fullmatch(r"\s*- '([^']+)'\s*",line)
        if not m:raise ValueError("unsupported upstream syntax")
        host=m[1];suffix=host.startswith("+.");host=host[2:] if suffix else host
        if len(host)>253 or not re.fullmatch(r"[A-Za-z0-9_-]+(?:\.[A-Za-z0-9_-]+)*",host):raise ValueError("unsupported domain pattern")
        row=("DOMAIN-SUFFIX," if suffix else "DOMAIN,")+host.lower()
        if row not in seen:rows.append(row);seen.add(row)
    if not 50000<=len(rows)<=500000:raise ValueError("unexpected source size; review manually")
    return rows

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--root",type=Path,default=Path(__file__).resolve().parents[1]);ap.add_argument("--revision");ap.add_argument("--input",type=Path);args=ap.parse_args()
    rev=args.revision or json.loads(fetch("https://api.github.com/repos/"+REPO+"/commits/release"))["sha"]
    if not re.fullmatch("[0-9a-f]{40}",rev):raise ValueError("invalid source revision")
    url="https://raw.githubusercontent.com/"+REPO+"/"+rev+"/direct.txt"
    body=args.input.read_bytes() if args.input else fetch(url);rows=convert(body)
    upstream_entries=len(rows)
    local_file=args.root/"rules"/"ChinaDirectDomains.local.list"
    local_rows=[]
    if local_file.exists():
        for line in local_file.read_text().splitlines():
            row=line.strip()
            if not row or row.startswith("#"):continue
            fields=row.split(",")
            if row=="IP-CIDR,100.64.0.0/10,no-resolve":pass
            elif len(fields)==2 and fields[0] in {"DOMAIN","DOMAIN-SUFFIX"} and re.fullmatch(r"[A-Za-z0-9_-]+(?:\.[A-Za-z0-9_-]+)*",fields[1]):pass
            else:raise ValueError("unreviewed local rule syntax")
            if row not in local_rows:local_rows.append(row)
    # Local domain rows are reviewed inputs, not a blanket union of candidates.
    # Preserve upstream host granularity and append only missing local rules.
    rows.extend(row for row in local_rows if row not in rows)
    target=args.root/"rules"/"ChinaDirectDomains.list";old=[]
    if target.exists():old=[x for x in target.read_text().splitlines() if x and not x.startswith("#")]
    header="# Source: "+url+"\n# License: GPL-3.0; see ChinaDirectDomains.LICENSE\n# Full reviewed snapshot; explicit owner proxy rules take priority.\n"
    output=(header+"\n".join(rows)+"\n").encode();target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(output)
    meta={"source_repository":REPO,"source_revision":rev,"source_file":"direct.txt","source_sha256":hashlib.sha256(body).hexdigest(),"generated_sha256":hashlib.sha256(output).hexdigest(),"entries":len(rows),"exact":sum(x.startswith("DOMAIN,") for x in rows),"suffix":sum(x.startswith("DOMAIN-SUFFIX,") for x in rows),"license":"GPL-3.0","upstream_entries":upstream_entries,"local_entries":len(local_rows),"local_file":"rules/ChinaDirectDomains.local.list","local_sha256":hashlib.sha256(local_file.read_bytes()).hexdigest() if local_file.exists() else None,"ip_cidr":sum(x.startswith("IP-CIDR,") for x in rows),"refresh":"daily 03:00 Asia/Hong_Kong; reviewed changes only; see rules/MAINTENANCE.md"}
    (target.parent/"ChinaDirectDomains.source.json").write_text(json.dumps(meta,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps({"revision":rev,"entries":len(rows),"added":len(set(rows)-set(old)),"removed":len(set(old)-set(rows))}))
if __name__=="__main__":main()
