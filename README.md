# SR

CN routes Ascott's verified first-party `discoverasr.com` and
`the-ascott.com` hostnames through the existing `rules/JPServices.list` and
`🇯🇵 JP REA`, ahead of mainland-IP routing. Each hostname has one rule owner.
Their shared CDN/cloud IPs are not fixed rules: one IP may serve unrelated
sites and may change without notice. The generated Clash subscription should
inherit the same domain rules; the OS profile is managed separately.

Personal CN split DNS: after a JP/MY/US list edit, run `python3 tools/build_cn_lite.py` then `python3 tools/build_cn_lite.py --check`. Include CN.conf, its alias and both manifests in the same release. Regeneration adds/removes exact and suffix Host mappings; never project bare IPs or ASNs. Clients must refresh the main SR profile, not just rule providers.
