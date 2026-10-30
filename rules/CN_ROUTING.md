# CN / CNR routing priorities

Mainland games use ChinaGamesDirect before the broad Proxy list. It contains
259 reviewed domain entries from pinned V2Fly category-games-cn and observed
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
