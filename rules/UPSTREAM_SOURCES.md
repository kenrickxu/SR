# Reviewed upstream rule sources

Reviewed: 2026-09-12

- yfamilys source repository snapshot: `b395bcd38c5163b30712ebb1213f0501fb435222`
- blackmatrix7 cross-check snapshot: `0087bb74e91b335e17a79fd07a8514277f7d77b4`

These files are owner-controlled snapshots used by CN.conf and OS.conf. They are
not automatically synchronized. Future upstream changes must be compared and
reviewed before publication.

| Local file | Profile and policy | Snapshot source | Cross-check source |
|---|---|---|---|
| ChinaMedia.list | CN DIRECT | deezertidal/shadowrocket-rules | blackmatrix7/ios_rule_script |
| ChinaDomain.list | CN DIRECT domain set | not published by yfamilys | blackmatrix7/ios_rule_script |
| China.list | CN DIRECT | deezertidal/shadowrocket-rules | blackmatrix7/ios_rule_script |
| Proxy.list | CN JP REA | deezertidal/shadowrocket-rules | blackmatrix7/ios_rule_script |
| DouYin.list | OS DIRECT | deezertidal/shadowrocket-rules | blackmatrix7/ios_rule_script |
| TikTok.list | OS DIRECT | deezertidal/shadowrocket-rules | blackmatrix7/ios_rule_script |
| TencentVideo.list | OS CN | deezertidal/shadowrocket-rules | blackmatrix7/ios_rule_script |
| WeChat.list | OS DIRECT | deezertidal/shadowrocket-rules | blackmatrix7/ios_rule_script |
| iQIYI.list | OS CN | deezertidal/shadowrocket-rules | blackmatrix7/ios_rule_script |
| Youku.list | OS CN | deezertidal/shadowrocket-rules | blackmatrix7/ios_rule_script |

## Review decisions

- On 2026-09-20, promoted the six WeChat domains not otherwise covered by the
  CN DIRECT domain sets (`slife.xy-asia.com`, `iot-tencent.com`,
  `wechatlegal.net`, `wechatos.net`, `wechatpay.com`, `weixinsxy.com`) and the
  missing DouYin video suffix `idouyinvod.com` into the early
  `ChinaEssentialsDirect.list`. This makes both routing and DIRECT system-DNS
  selection explicit without adding another top-level rule set. The same audit
  found complete existing CN DIRECT coverage for the maintained TencentVideo,
  iQIYI, Youku, HunanTV and BiliBili sets: 209/209 domains and 62/62 explicit
  IP ranges, so no duplicate media rules were added.
- On 2026-09-19, omitted 22 later `ChinaMedia.list` entries and 108 later
  `ChinaDomain.list` suffixes that were fully covered by earlier CN `DIRECT`
  suffix rules (107 exact hosts and 23 child domains). The first-match policy
  and rule order are unchanged. Upstream metadata in `ChinaDomain.list` still
  describes the original snapshot; future upstream reviews must compare against
  that source before reapplying the local dedup filter.
- Added the missing paired China domain set (3,580 current entries after the
  2026-09-19 local dedup filter). The
  yfamilys China.list contains only mixed non-domain rules; using DOMAIN-SET
  restores the maintained mainland-domain half without expanding each domain
  into an individual top-level rule.
- Added `DOMAIN,btrace.qq.com` to WeChat because it exists in the newer
  blackmatrix7 list but was missing from the yfamilys snapshot.
- Kept yfamilys IPv6 rule-type corrections and its additional TikTok process and
  WeChat IP coverage. Corrected 29 remaining TencentVideo IPv4-mapped IPv6
  entries from `IP-CIDR` to `IP-CIDR6`.
- Removed four CN same-policy user-agent duplicates from the later China list;
  they remain in the earlier ChinaMedia list.
- Removed the foreign `.ms` country-code suffix from the China DIRECT list and
  removed six narrower CIDRs already fully covered by broader DIRECT CIDRs.
- Removed the malformed `origin-a.akamaihd.ne` exact-domain entry while
  retaining the valid `origin-a.akamaihd.net` entry.
- Removed `USER-AGENT,hearthstone*` from the later Proxy list because the
  earlier China list already intentionally resolves it to DIRECT.
- Removed `snssdk.com` from the later TikTok list because the earlier DouYin
  list already resolves it to DIRECT.
- Removed `dldir1.qq.com` and `soup.v.qq.com` from the later WeChat list
  because the earlier TencentVideo list intentionally owns those shared video
  endpoints through the CN policy.
- Case variants such as `iQIYI*` / `iQiyi*` are retained because user-agent
  matching behavior can be case-sensitive.

## Attribution

- deezertidal/shadowrocket-rules: https://github.com/deezertidal/shadowrocket-rules
- blackmatrix7/ios_rule_script is distributed under GPL-2.0:
  https://github.com/blackmatrix7/ios_rule_script/blob/master/LICENSE
