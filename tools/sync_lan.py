#!/usr/bin/env python3
"""Generate reviewed owner-hosted blackmatrix7 LAN rules; never deploys or schedules."""
import argparse,urllib.request,json,re,hashlib,ipaddress
from pathlib import Path
REPO="blackmatrix7/ios_rule_script"
SOURCE="rule/Shadowrocket/Lan/Lan.list"
def fetch(url):
    return urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"Ken-SR-Lan-maintenance"}),timeout=30).read()
def generate(body,revision):
    rows=[];native=[];counts={};seen=set()
    for line in body.decode("utf-8-sig").splitlines():
        row=line.strip()
        if not row or row.startswith("#"):continue
        a=row.split(",");kind=a[0]
        if kind in {"IP-CIDR","IP-CIDR6"}:
            if len(a)!=3 or a[2]!="no-resolve":raise ValueError("LAN IP options invalid")
            n=ipaddress.ip_network(a[1],strict=True)
            native.append(("IP-CIDR6" if n.version==6 else "IP-CIDR")+","+a[1]+",no-resolve")
        elif kind in {"DOMAIN","DOMAIN-SUFFIX"}:
            if len(a)!=2 or not re.fullmatch(r"[A-Za-z0-9_.-]{1,253}",a[1]):raise ValueError("LAN domain invalid")
            native.append(row)
        else:raise ValueError("LAN syntax unsupported")
        if row in seen:raise ValueError("LAN duplicate row")
        seen.add(row);rows.append(row);counts[kind]=counts.get(kind,0)+1
    if not 100<=len(rows)<=1000:raise ValueError("unexpected LAN list size; review manually")
    header=("# Owner mirror of https://github.com/"+REPO+"\n# Source revision: "+revision+"\n# License: GPL-2.0; see Lan.LICENSE\n").encode()
    sr=header+body
    clash=header+b"# Native Mihomo conversion: IPv6 IP-CIDR -> IP-CIDR6; no IPv6 enable switch.\n"+("\n".join(native)+"\n").encode()
    meta={"repository":REPO,"file":SOURCE,"revision":revision,"upstream_sha256":hashlib.sha256(body).hexdigest(),"sr_sha256":hashlib.sha256(sr).hexdigest(),"clash_sha256":hashlib.sha256(clash).hexdigest(),"rows":len(rows),"types":counts,"ipv6_rows":sum(x.startswith("IP-CIDR6,") for x in native),"refresh":"daily 03:00 Asia/Hong_Kong; compare additions/removals; see rules/MAINTENANCE.md"}
    return sr,clash,meta

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--root",type=Path,default=Path(__file__).resolve().parents[1]);ap.add_argument("--revision");ap.add_argument("--input",type=Path);a=ap.parse_args()
    rev=a.revision or json.loads(fetch("https://api.github.com/repos/"+REPO+"/commits?path="+SOURCE+"&per_page=1"))[0]["sha"]
    if not re.fullmatch("[0-9a-f]{40}",rev):raise ValueError("invalid source revision")
    body=a.input.read_bytes() if a.input else fetch("https://raw.githubusercontent.com/"+REPO+"/"+rev+"/"+SOURCE)
    sr,clash,meta=generate(body,rev);dest=a.root/"rules";dest.mkdir(parents=True,exist_ok=True)
    old=(dest/"Lan.list").read_text().splitlines() if (dest/"Lan.list").exists() else []
    old={x for x in old if x and not x.startswith("#")};new={x for x in sr.decode().splitlines() if x and not x.startswith("#")}
    (dest/"Lan.list").write_bytes(sr);(dest/"LanClash.list").write_bytes(clash);(dest/"Lan.source.json").write_text(json.dumps(meta,indent=2)+"\n")
    print(json.dumps({"rows":meta["rows"],"added":len(new-old),"removed":len(old-new),"ipv6_translated":meta["ipv6_rows"]}))
if __name__=="__main__":main()
