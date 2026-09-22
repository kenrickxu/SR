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
| ByteDanceGlobal.list | CN JP REA / OS DIRECT | reviewed shared subset | DouYin / TikTok snapshots |
| DouYin.list | CN DIRECT / OS DIRECT | reviewed domestic-first subset | DouYin / ChinaDomain snapshots |
| TikTok.list | CN JP REA / OS DIRECT | reviewed international subset | TikTok snapshots |
| TencentVideo.list | OS CN | deezertidal/shadowrocket-rules | blackmatrix7/ios_rule_script |
| WeChatCore.list | CN DIRECT / OS DIRECT | reviewed shared subset | WeChat snapshots |
| WeChat.list | OS DIRECT | deezertidal/shadowrocket-rules | blackmatrix7/ios_rule_script |
| iQIYI.list | OS CN | deezertidal/shadowrocket-rules | blackmatrix7/ios_rule_script |
| Youku.list | OS CN | deezertidal/shadowrocket-rules | blackmatrix7/ios_rule_script |

## Review decisions

- On 2026-09-22, added the two observed Tencent/Aceville WeChat HTTPDNS ranges
  `43.160.156.0/23` and `101.32.133.0/24` to `WeChatCore`. Recent CN connection
  logs showed 65 raw TCP requests to these ranges interleaved with WeChat
  traffic; because those requests exposed only an IP, they previously missed
  the domain rules and fell through to the JP final policy. Both ranges now use
  the existing shared DIRECT provider in CN and OS without loading the broad
  318-entry `WeChat.list` into CN or changing DNS.
- On 2026-09-22, made the Douyin/TikTok split explicit. `DouYin.list` owns the
  unambiguous Douyin roots plus shared `bytedapm.com`/`ibytedapm.com`; those
  roots were removed from `ChinaDomain` and `TikTok` so domestic app traffic
  matches the early DIRECT list once. CN imports the remaining international
  `TikTok.list` through `JP REA`, while OS imports DouYin, ByteDanceGlobal and
  TikTok as DIRECT. The owner prioritizes domestic Douyin when a ByteDance
  infrastructure suffix is shared by both apps.
- On 2026-09-22, removed all 151 exact cross-file rule duplicates across the
  original 17 owner lists. Canonical ownership is now service-specific: DouYin,
  TencentVideo, iQIYI, Youku and EZVIZ retain their own rules, while
  `ChinaMedia`, `ChinaEssentialsDirect`, `JPServices` and `China` no longer
  repeat them. The two shared ByteDance domains now live only in
  `ByteDanceGlobal.list`, which CN assigns to `JP REA` and OS assigns to
  `DIRECT`; TikTok remains profile-specific without a copied domain. The 13
  shared WeChat entries now live only in `WeChatCore.list`, so CN avoids loading
  the full 318-entry OS WeChat IP-prefix list. CN imports the remaining five
  mainland service lists directly as `DIRECT`. This preserves OS
  policy differences without duplicating rule definitions. Broader parent/
  child matches such as `qq.com` and `weixin.qq.com` remain where profiles need
  different application scopes; they are not identical duplicate rules.
- On 2026-09-20, classified nine observed CN-profile DNS roots without changing
  the profile DNS policy. Added `ndcpp.com`, `yingt.fun`, `puata.info`,
  `qiezibenpao.com` and `rtcxyz.com` to the early CN DIRECT provider so all
  subdomains use the existing DIRECT/system-DNS path. Added `ggpht.com`,
  `app-analytics-services.com`, `sentry.io` and `revenuecat.com` to the early
  JP provider so all subdomains avoid GEOIP/final-rule ambiguity. These are
  intentionally `DOMAIN-SUFFIX` entries; Ali DoH, General, proxy groups and
  protected MITM remain unchanged.
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
- Added the missing paired China domain set (3,567 current entries after the
  2026-09-19 and 2026-09-22 local dedup filters). The
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
