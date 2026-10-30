# CN / CNR routing priorities

Mainland games use ChinaGamesDirect before the broad Proxy list. It contains
263 reviewed domain entries from pinned V2Fly category-games-cn and observed
Delta Force China endpoints. International game editions, global SDK roots and
shared cloud address ranges are excluded. ChinaDomain/China/GEOIP CN remain
DIRECT fallbacks; unknown future games still require evidence-based review.

ApplePushProxy precedes AppleDirect: CN uses JP REA; CNR uses US. It includes
push.apple.com and Apple's published APNs-specific IPv4/IPv6 ranges. Other
Apple services keep their existing DIRECT policy. APNs is shared by apps, so
this changes the Apple push transport for all apps, not just Telegram.

Canonical Clash imports the CN compatible owner lists through filtered
/sr-rules/ endpoints. CNR is the separate Shadowrocket profile; no CNR Clash
output is changed. Primary DNS, node identities and MITM settings are retained
in CN.conf and CNR.conf. OS is separate.

DNS fallback clarification (owner-tested Shadowrocket 2.2.93, 2026-10-30):
CN and CNR explicitly set dns-fallback = false for the Enable Fallback switch.
Keep dns-fallback-system = false as a compatibility guard and leave
fallback-dns-server = empty: this is an address list, not a boolean. It does
not need AliDNS or system added while fallback is disabled. DIRECT still uses
system DNS; the primary DNS pool remains 223.5.5.5,223.6.6.6. This supersedes
the earlier assumption that dns-fallback-system alone controlled the UI.
These Shadowrocket keys must not be copied into Clash YAML; canonical Clash
already has no fallback or fallback-filter. Refresh both remote profiles;
route policies, providers, node identities and MITM are unaffected.

After publishing, refresh both the profile and its rule sets; reconnect the
VPN once to replace old persistent APNs connections. Check actual iPhone
locked-screen push and national-server gameplay separately from syntax tests.

Sources: https://support.apple.com/en-us/102266 and
https://github.com/v2fly/domain-list-community/tree/333d8a1810d04600bcb00870155a369954ed37f5/data

Owner 2026-10-30 supersedes the US-TUIC default: CN and canonical Clash US
routes use US REA with US-Reality as the only regional group member. TUIC
nodes remain in the subscription and the separate TUIC game selector remains
available. A new regional group name avoids restoring a cached TUIC choice.
CNR keeps its separate US Reality policy.
TencentVideoCN is the CN/CNR mirror excluding three benchmark/fake mapped
addresses; the shared OS list remains independent. Canonical Clash respects
the same ordering, including model downloads, AI, OKX and infrastructure IPs.

Owner-approved game compatibility follow-up (2026-10-31): pvp.qq.com,
gp.qq.com and smoba.qq.com explicitly join the early DIRECT game list. The
observed download.2.1212338883.wz.gcloudgbs.com host is also early DIRECT
after a same-LAN DNS comparison; dir.1212338883-2-1.gcloudsvcs.com retains
its existing GEOIP CN DIRECT fallback because its cold system sample was
slower. CN/CNR add fourteen exact observed non-qq game/SDK hosts to
always-real-ip; canonical Clash maps these to native fake-ip-filter entries.
Existing *.qq.com coverage, skip-proxy, DNS pools/system-direct/no-fallback,
IPv6, APNs routing, nodes and protected MITM stay intact. These entries
reduce address compatibility uncertainty; they do not prove a latency gain
or that the original logs misrouted gameplay. Device gameplay acceptance
requires a separate same-iPhone Wi-Fi/5G comparison.

CN-only inline game trial (owner request, 2026-10-31): CN.conf replaces the
ChinaGamesDirect RULE-SET reference with a local snapshot at the same
priority. From the reviewed263 game entries, the owner explicitly replaces
10 tcdnos.com child rules with one DOMAIN-SUFFIX,tcdnos.com,DIRECT.
The resulting local game block has254 rows; apex and all descendants
use DIRECT. always-real-ip contains tcdnos.com and *.tcdnos.com, replacing
covered exact children. Other services under that parent also follow this
owner policy; it is not a guarantee of mainland-only server locations.
Inline removes one remote-list dependency, not routing decisions, and is not
a measured packet-speed improvement. Keep its base source hash; future shared
game-list changes require explicit CN snapshot reconciliation. Other rule sets,
IP/ASN/GEOIP fallbacks, DNS, nodes, protected MITM and skip-proxy stay intact.
skip-proxy chooses HTTP-proxy versus TUN handling; it is not a UDP TUN bypass.
Do not add ephemeral game IP pins or public TUN exclusions without evidence.
The new connection log has105 UDP entries allDIRECT; the DNS database is empty.
The owner reports Wi-Fi ping30->70/100ms; same-phone SR-off/on and network
comparison is still required for causal diagnosis. Desktop ICMP is not game RTT.
CNR, its shared game provider and canonical Clash are unchanged by explicit
owner scope; Clash stays pinned to SR41d90d1. Do not apply this CN-only trial
to Clash without a later owner request.
