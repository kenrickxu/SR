"""Project proxy-domain selectors into Shadowrocket Host DNS entries during profile build."""
import re
from pathlib import Path
BEGIN='# BEGIN GENERATED PROXY DNS'
END='# END GENERATED PROXY DNS'

def render(root, text):
    # Deterministic order also preserves MY > US > JP precedence for exact duplicates.
    entries={}
    for region in ('MY','US','JP'):
        resolver='1.1.1.1' if region=='JP' else '1.0.0.1'
        for line in (root/f'rules/{region}Proxy.list').read_text().splitlines():
            row=line.partition('#')[0].strip().split(',')
            if row[0] not in ('DOMAIN','DOMAIN-SUFFIX'): continue
            assert len(row)==2 and re.fullmatch(r'[a-zA-Z0-9._-]+',row[1]),row
            name=row[1].lower()
            entries.setdefault(name,resolver)
            if row[0]=='DOMAIN-SUFFIX':entries.setdefault('*.'+name,resolver)
    block=BEGIN+'\n'+''.join(f'{k} = server:{v}\n' for k,v in sorted(entries.items()))+END
    assert text.count(BEGIN)==text.count(END)==1
    return re.sub(re.escape(BEGIN)+'.*?'+re.escape(END),lambda _:block,text,flags=re.S)
