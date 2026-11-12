#!/usr/bin/env python3
"""Check canonical SR Lite and synchronize its compatibility alias, not the archived full profile."""
from pathlib import Path
import argparse,hashlib,json,re,ipaddress
CANONICAL='https://sr-config.kt7766.org/CN.conf'
ALIAS='https://raw.githubusercontent.com/kenrickxu/SR/main/CN-Lite.conf'
ARCHIVE='archive/cn-full-20261112-7106fd4'

def derive(root):
    raw=(root/'CN.conf').read_bytes();text=raw.decode();rules=[r.strip()for r in text.split('[Rule]',1)[1].split('[',1)[0].splitlines()if r.strip()and not r.lstrip().startswith('#')]
    assert 'ChinaDirectDomains.list'not in '\n'.join(rules),'Canonical CN must remain Lite; full data lives in the reference archive'
    assert rules[-2:]==['GEOIP,CN,DIRECT','FINAL,🇯🇵 JP REA']
    prefix=['RULE-SET,https://sr-config.kt7766.org/rules/'+n+'.list,'+policy for n,policy in [('MYProxy','🇲🇾 MY REA'),('USProxy','🇺🇸 US REA'),('JPProxy','🇯🇵 JP REA'),('AppleDirect','DIRECT')]]
    off=1 if rules[0].startswith('AND,')else 0
    assert rules[off:off+4]==prefix
    direct=rules[off+4:-2];assert direct and len(direct)==len(set(direct))
    for row in direct:
        a=row.split(',')
        if a[0]in ['DOMAIN','DOMAIN-SUFFIX']:assert len(a)==3 and a[2]=='DIRECT'and re.fullmatch('[A-Za-z0-9_.-]+',a[1])
        else:assert row=='IP-CIDR,100.64.0.0/10,DIRECT,no-resolve'
    for key in ['tun-excluded-routes','always-real-ip','skip-proxy']:assert len(re.findall('^'+key+' = ',text,re.M))==1
    routes=re.search('^tun-excluded-routes = (.+)$',text,re.M)[1].split(',');assert len(routes)==len(set(routes))
    for route in routes:ipaddress.ip_network(route,strict=True)
    assert '17.0.0.0/8'not in routes and '127.0.0.0/8'not in routes
    assert re.search('^update-url = (.+)$',text,re.M)[1]==CANONICAL
    alias=re.sub('^update-url = .+$',lambda _:'update-url = '+ALIAS,text,flags=re.M).encode()
    sourcefiles=['CN.conf']+['rules/'+n+'.list'for n in ['MYProxy','USProxy','JPProxy','AppleDirect']]
    hashes={f:hashlib.sha256((root/f).read_bytes()).hexdigest()for f in sourcefiles}
    meta={'schema':2,'mode':'canonical-sr-lite','profile':'CN.conf','profile_sha256':hashlib.sha256(raw).hexdigest(),'source_sha256':hashes,'direct_subset_rows':len(direct),'direct_domain_rows':len(direct)-1,'full_reference':'CN-Full.conf','full_exact_archive':ARCHIVE,'policy':'Canonical SR is Lite; retain Game TUN/RealIP/Skip and media/Push priorities; full provider retained only for other consumers/reference.','native_runtime_applied':False,'limitations':['Unlisted domestic services on overseas IPs may proxy.','DIRECT media is not full TUN bypass.','Phone RAM, future game IPs and notification/call outcomes require client acceptance.']}
    aliasmeta={**meta,'profile':'CN-Lite.conf','profile_sha256':hashlib.sha256(alias).hexdigest(),'canonical':'CN.conf'}
    return {'CN-Lite.conf':alias,'CN.source.json':(json.dumps(meta,ensure_ascii=False,indent=2)+'\n').encode(),'CN-Lite.source.json':(json.dumps(aliasmeta,ensure_ascii=False,indent=2)+'\n').encode()}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parent.parent);ap.add_argument('--check',action='store_true');a=ap.parse_args();outputs=derive(a.root)
    for name,body in outputs.items():
        f=a.root/name
        if a.check:assert f.read_bytes()==body,'Stale derived '+name
        else:f.write_bytes(body)
    print(json.dumps({'check':a.check,'canonical_mode':'sr-lite','alias_bytes':len(outputs['CN-Lite.conf']),'full_reference_modified':False}))
if __name__=='__main__':main()
