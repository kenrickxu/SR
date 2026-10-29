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
output is changed. DNS, node identities and MITM settings are unchanged in
CN.conf and CNR.conf. OS is separate.

After publishing, refresh both the profile and its rule sets; reconnect the
VPN once to replace old persistent APNs connections. Check actual iPhone
locked-screen push and national-server gameplay separately from syntax tests.

Sources: https://support.apple.com/en-us/102266 and
https://github.com/v2fly/domain-list-community/tree/333d8a1810d04600bcb00870155a369954ed37f5/data
