# Owner-hosted mainland/direct domain snapshot

## Mainland DIRECT, owner exceptions, default proxy — 2026-11-06

Ken approved this design in SR Topic194 message1251. It supersedes
`CN_LIGHTWEIGHT_PROXY_V1` default DIRECT, not the rest of the profiles.
CN/CNR use marker `CN_CHINA_DIRECT_V1`; JP native manifest layout is
`china-direct-proxy-v1`.

Order: local/private destinations (and CNR owner-management DIRECT isolation),
existing explicit domain/keyword/IPv4 JP/US exceptions, one owner-hosted
`ChinaDirectDomains.list` DIRECT rule set, GEOIP CN DIRECT, default JP in
CN/Clash and US in CNR. Existing proxy overlaps intentionally win over the
mainland domain list. OS is not changed.

ChinaDirectDomains.list is the complete Loyalsoldier/clash-rules direct.txt
snapshot converted without broadening: upstream `+.domain` becomes
DOMAIN-SUFFIX, plain host becomes DOMAIN. Never strip subdomains from plain
upstream entries: that would incorrectly expand direct access. These are
mainland/direct-connectivity classifications, not legal nationality or a
complete definition of every foreign site. Retain existing explicit Google,
Apple push, OKX and other owner proxy exceptions ahead of the provider.
The overlap report is ChinaDirectDomains.overrides.json; snapshot revision,
source/output SHA256 and counts are ChinaDirectDomains.source.json.
GPL-3.0 attribution/license is kept in ChinaDirectDomains.LICENSE.

Maintenance is manual when Ken requests it. Run tools/sync_china_direct.py,
review both additions and removals plus exceptions, update the overlap report,
and commit/revalidate all consumers. The script only writes repository files;
it never schedules, publishes or updates a remote service by itself. Do not
silently subscribe clients to changing upstream URLs: clients use Ken's own
GitHub list. Do not accumulate upstream files into CN/CNR inline rule tables.

Clash emits a native classical/text HTTP provider pointed at the same owner
GitHub list, fetched using JP REA with the existing 86400s refresh interval.
It does not pass the huge list through the old JP filtered rule cache/inline
provider path. Preserve whole General/DNS/TUN/Host/node/MITM settings: no bulk
real-IP/TUN exclusions or application identity rules restored. CNR's five
previously omitted owner IP selectors are now explicit DIRECT so US default
does not unintentionally capture them. All existing explicit CN/CNR proxy
rows remain, in their old relative order; no unrelated business reassignment.

Source publication, native parser/provider acceptance, client refresh and
actual phone use are separate. No promises about gaming speed or browser
verification follow from rule counts. Refresh selected CN/CNR configs and the
new rule set; refresh Clash subscription/provider and confirm rule mode.
Rollback is a new GitHub revert of this change plus the matching JP code and
manifest transaction backup, not a force-push or whole old-profile restore.

