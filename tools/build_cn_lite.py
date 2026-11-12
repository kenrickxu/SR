#!/usr/bin/env python3
"""Derive the opted-in SR-only Lite profile from current authoritative inputs.
No fetch, native-runtime apply, secret output, new background producer or guessing.
"""
from pathlib import Path
import argparse,hashlib,json,re
URL='https://raw.githubusercontent.com/kenrickxu/SR/main/CN-Lite.conf'

def derive(root):
    raw=(root/'CN.conf').read_bytes();base=raw.decode();real=re.search(r'^always-real-ip = (.+)$',base,re.M)[1].split(',');realset=set(real)
    files=['CN.conf']+['rules/'+n+'.list'for n in ['ChinaDirectDomains','AppleDirect','USProxy','JPProxy','MYProxy']]
    rows=lambda name:[l.strip()for l in(root/('rules/'+name+'.list')).read_text().splitlines()if l.strip()and not l.lstrip().startswith('#')]
    china=rows('ChinaDirectDomains');apple=rows('AppleDirect')
    domains=lambda rr,kind:{l.split(',')[1]for l in rr if l.startswith(kind+',')}
    cs,ce=domains(china,'DOMAIN-SUFFIX'),domains(china,'DOMAIN');aps,ape=domains(apple,'DOMAIN-SUFFIX'),domains(apple,'DOMAIN')
    def covered(host,suffixes,exact=()):
        return host in exact or any('.'.join(host.split('.')[i:])in suffixes for i in range(len(host.split('.'))))
    candidates=['DOMAIN-SUFFIX,cn']if 'cn'in cs else[];held=[]
    for host in real:
        if host.startswith('*.'):continue
        wildcard='*.'+host in realset
        if covered(host,aps,ape)and (not wildcard or covered(host,aps)):continue
        if covered(host,cs,ce)and(not wildcard or covered(host,cs)):
            candidates.append(('DOMAIN-SUFFIX,'if wildcard else'DOMAIN,')+host)
        else:held.append(host)
    suffixes=domains(candidates,'DOMAIN-SUFFIX');small=[]
    for row in candidates:
        kind,host=row.split(',');start=0 if kind=='DOMAIN'else 1
        if any('.'.join(host.split('.')[i:])in suffixes for i in range(start,len(host.split('.')))):continue
        if row not in small:small.append(row)
    ip='IP-CIDR,100.64.0.0/10,no-resolve';assert china.count(ip)==1;small.append(ip)
    needle='RULE-SET,https://sr-config.kt7766.org/rules/ChinaDirectDomains.list,DIRECT';assert base.count(needle)==1
    direct=lambda row:','.join(row.split(',')[:2]+['DIRECT']+row.split(',')[2:])
    replacement='# SR Lite: reviewed common-domain subset; other destinations use GeoIP/fallback.\n'+'\n'.join(direct(row)for row in small)
    out=base.replace(needle,replacement);assert len(re.findall(r'^update-url = .+$',out,re.M))==1
    out=re.sub(r'^update-url = .+$',lambda _: 'update-url = '+URL,out,flags=re.M)
    # All original proxy/media rules and route/RealIP/Skip strings stay intact.
    for key in ['tun-excluded-routes','always-real-ip','skip-proxy']:
        assert re.search('^'+key+' = .+$',out,re.M)[0]==re.search('^'+key+' = .+$',base,re.M)[0]
    for row in small:
        kind,host,*rest=row.split(',')
        assert row==ip or (covered(host,cs)if kind=='DOMAIN-SUFFIX'else covered(host,cs,ce))
    hashes={name:hashlib.sha256((root/name).read_bytes()).hexdigest()for name in files}
    meta={'schema':1,'profile':'CN-Lite.conf','source_sha256':hashes,'profile_sha256':hashlib.sha256(out.encode()).hexdigest(),'direct_subset_rows':len(small),'direct_domain_rows':len(small)-1,'source_mainland_rows':len(china),'held_real_ip_hosts':held,'policy':'SR-only opted-in common-domain subset; preserve original TUN/RealIP/Skip, media and proxy order. Full CN retained separately.','limitations':['Unknown mainland-domain services on non-CN IPs may now proxy.','DIRECT media is not proof of TUN bypass.','Client module/runtime settings and future game IPs require phone verification.'],'native_consumers_changed':False}
    return out.encode(),(json.dumps(meta,ensure_ascii=False,indent=2)+'\n').encode(),meta

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parent.parent);parser.add_argument('--check',action='store_true');args=parser.parse_args()
    body,meta,summary=derive(args.root)
    for name,data in [('CN-Lite.conf',body),('CN-Lite.source.json',meta)]:
        target=args.root/name
        if args.check:assert target.read_bytes()==data,'Stale '+name+'; run tools/build_cn_lite.py in the same source checkout'
        else:target.write_bytes(data)
    print(json.dumps({'check':args.check,'profile_bytes':len(body),'direct_rows':summary['direct_subset_rows'],'native_consumers_changed':False}))
if __name__=='__main__':main()
