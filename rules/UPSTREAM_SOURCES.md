# Reviewed upstream rule sources

Reviewed: 2026-09-23

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
| USAI.list | CN US / OS DIRECT | owner-maintained AI service roots | current CN and OS routing audit |
| TencentMeeting.list | CN DIRECT / OS DIRECT | owner connection-log evidence | Tencent Meeting firewall guide |
| TencentVideo.list | OS CN | deezertidal/shadowrocket-rules | blackmatrix7/ios_rule_script |
| WeChatCore.list | CN DIRECT / OS DIRECT | reviewed shared subset | WeChat snapshots |
| WeChat.list | OS DIRECT | deezertidal/shadowrocket-rules | blackmatrix7/ios_rule_script |
| iQIYI.list | OS CN | deezertidal/shadowrocket-rules | blackmatrix7/ios_rule_script |
| Youku.list | OS CN | deezertidal/shadowrocket-rules | blackmatrix7/ios_rule_script |

## Review decisions

- Follow-up 2026-10-26: owner explicitly requested the entire kt7766.org
  domain through VPN in CN/CNR/Clash, superseding the exact-host decision
  below. Remove DOMAIN-SUFFIX,kt7766.org from BusinessDirect and replace the
  exact t.kt7766.org rule with one parent DOMAIN-SUFFIX rule: CN/Clash JP REA,
  CNR US. No retained child duplicate or opposite DIRECT entry. OS does not
  import BusinessDirect, so OS and its providers remain unchanged. Node
  connection parameters and credentials are unchanged.

- On 2026-10-26, owner reported Tiffany SR update failures while Kenrick
  worked and approved proxying subscription downloads. Existing BusinessDirect
  DOMAIN-SUFFIX,kt7766.org forces all account URLs DIRECT. Add exact
  DOMAIN,t.kt7766.org before service sets in CN (JP REA) and CNR (US);
  canonical Clash imports the CN JP exception. Preserve the broad DIRECT
  suffix for other subdomains and OS. All nine ordinary account payloads
  validate from origin/public; this is a confirmed routing weakness, not proof
  that China Unicom caused the reported failure. Account tokens/credentials,
  General/DNS/IPv6 and node configuration remain unchanged. Client must first
  load the new profile and enable a working node before retrying subscription.

- Follow-up 2026-10-26, owner approved widening the Tencent Meeting DIRECT
  domain scope from media.tencentmeeting.com to tencentmeeting.com. Replace
  the narrower suffix in ChinaEssentialsDirect, already consumed before Proxy
  by CN/CNR and canonical Clash; do not duplicate the child suffix. This covers
  the apex and every descendant, including future subdomains, but does not
  imply all servers are mainland or cover other roots/raw-IP connections.
  Retain the official Meeting IP supplement and existing Tencent/QQ routes.
  Provider entries remain 32; General/DNS/nodes/OS and generator unchanged.

- On 2026-10-26, audit domestic Tencent Meeting against official firewall JSON
  v1.14 dated 2026-07-10 (SHA256
  0391adf2e082f78baea2a8e56bca51f2939b03298bd7d1623bdcf72d6250c54e):
  https://meeting.tencent.com/support/topic/1929/index.html
  https://cdn.meeting.tencent.com/upload/firewall/domain_ip.json
  Of 238 distinct listed domains, only sso.media.tencentmeeting.com lacks an
  explicit DIRECT domain match in CN/CNR/canonical Clash. Add the published
  media.tencentmeeting.com suffix to ChinaEssentialsDirect. This is a coverage
  gap, not a claimed observed proxy connection: supplied logs contain only one
  identifiable Meeting connection (DIRECT) repeated across overlapping exports.
  Add TencentMeetingIPDirectCN with 160 explicit IP entries: 123 official /24s,
  32 IPv4 /32s and 5 IPv6 /128s. Select mainland-labelled media/whiteboard plus
  unlabelled common login/HTTPDNS/IM/MRA/disaster-recovery endpoints; common
  endpoints are not assumed geographically mainland. 174 unique selected
  networks minus 14 already covered by literal DIRECT CIDRs leaves 160.
  Exclude 68 region-labelled non-mainland rows. Preserve original prefix widths,
  no DNS-derived CDN IP pinning, no broader ASN expansion. Many selected IPs
  already use GEOIP/AS132203; these additions make their DIRECT intent explicit,
  not 160 demonstrated misroutes. Keep explicit Proxy ahead of this supplement,
  then WeChat IP/AS132203/GEOIP. Canonical Clash must restore this boundary after
  managed-rule injection. Shared TencentMeeting.list and OS stay unchanged.
  General/DNS/IPv6/real-IP/node/MITM settings are outside this change.

- Follow-up 2026-10-26 final iQIYI download audit (new export through 10:18):
  9,823 connections / 2,290 DNS records. All 1,461 identifiable iQIYI-related
  connections are DIRECT, including 172 OFFLINE and 139 video-file requests
  (overlapping subsets). Existing 34 iQIYI suffixes cover first-party services;
  the observed alikunlun.com CNAME is also covered by ChinaDomain's suffix.
  No video route leak was found. Two empty DNS answers belong to one masked
  afdback.ppsimg.com host, not an identified download CDN. Logs contain no
  throughput or transfer duration and cannot establish maximum download speed.
  Owner explicitly requested broader domestic suffix coverage: replace the
  three exact crt/crl/ocsp.sectigochina.com rows with DOMAIN-SUFFIX for
  sectigochina.com in ChinaEssentialsDirect. All its current and future child
  endpoints match DIRECT before Proxy trustd in CN, CNR and canonical Clash.
  This supersedes the exact-host-only restriction below for this one suffix.
  Remaining international CA hosts stay exact. No shared CDN/carrier IP expansion,
  no iQIYI shared-list change, and no OS change (including its imported lists).
  Refresh the filtered Clash provider cache as well as the managed source receipt;
  installed clients remain owner-refreshed. The 10:15:20 phone OCSP request still
  matched old trustd routing, so publication is not proof of client refresh.

- Follow-up 2026-10-26 media/certificate and four-profile precedence review:
  15 mainland video site TLS handshakes passed using direct TCP from Windows
  with TUN disabled; issuer/AIA/OCSP/CRL endpoints were read from the real leaf
  certificates. 25 direct endpoint probes returned HTTP 200; all 11 issuer/root
  files parsed as X509. Six real OCSP requests returned signed, verified GOOD
  responses (42-699ms). Root-path OCSP HTTP 200 alone was not counted as a
  valid certificate-status response. These are service probes, not playback
  or download-throughput measurements.
  ChinaEssentialsDirect gains 11 exact CA host exceptions: RapidSSL issuer,
  CRL/status, GlobalSign CRL/OCSP, Sectigo China CRL/OCSP, and the separately
  logged DigiCert/Sectigo OCSP, USERTrust issuer and Certum repository hosts.
  The two existing exact CA hosts remain. DigiCert .cn endpoints already use
  DIRECT via China.list; no broad CA/CDN/IP suffix or trustd-wide DIRECT rule
  is introduced. Public CA service references:
  https://www.sectigo.com/knowledge-base/detail/OCSP-and-CRL-access-information
  https://www.alibabacloud.com/help/en/ssl-certificate/download-a-root-certificate-and-an-intermediate-certificate
  CN/CNR place ChinaMedia with explicit domestic service sets, before generic
  keywords/proxy lists; DNS, node groups, MITM and service policies are intact.
  Canonical Clash must remove the obsolete DOUYIN canary's nine domain
  overrides, route its four domestic app processes DIRECT, and restore
  DouYin/TikTok/ChinaMedia provider precedence relative to imported owner
  rules. iCloud DIRECT must precede Microsoft shared-CDN proxy matching for
  www-cdn.icloud.com.akadns.net. Keep TikTok/international routes proxied and WeChat IP/ASN fallback
  after explicit proxy choices. Windows-specific groups are retained.
  OS remains an overseas DIRECT-default profile: Tencent Video/iQIYI/Youku
  and EZVIZ keep their explicit CN routes and extended matching, grouped
  before the broader WeChat DIRECT set. Five Tencent-video /128 exceptions
  precede overlapping WeChat prefixes by design. No mainland-wide OS catch-all
  or new media relay policy is introduced. Existing default DIRECT already
  covers the audited CA hosts; importing ChinaEssentials there would override
  its explicit Baidu/airline CN choices and is intentionally avoided.
  This supersedes only the earlier instruction to leave OS ordering unchanged.


- On 2026-10-26, audited 5,711 connection and 1,721 DNS records from the
  owner's 23:51 export (records continue through 09:33 the next morning).
  All 583 identifiable iQIYI connections, including 69 OFFLINE requests,
  already use DIRECT; 82 related DNS queries succeeded. Do not add broad
  carrier/CDN ranges or call this a proven video-throughput repair.
  ChinaEssentialsDirect adds only exact `crt.sectigochina.com` and
  `secure.globalsign.com`: three observed certificate fetches hit Proxy's
  `com.apple.trustd*` USER-AGENT rule despite mainland CDN availability.
  Native Windows curl with proxies bypassed and TUN disabled fetched the
  public certificates successfully from mainland CDN addresses. The same
  existing provider is DIRECT in CN, CNR and canonical Clash; OS does not
  import it. Preserve the remaining trustd policy, video rules, DNS, nodes,
  MITM and broad ASN policy. Client refresh and download-speed acceptance
  remain separate from source and native-core validation.

- Final owner override on 2026-10-25 supersedes the ASN exclusion and
  CNR-unchanged decisions below: CN and CNR now explicitly import
  `IP-ASN,132203,DIRECT,no-resolve` after the reviewed WeChat IP supplement.
  CNR now also imports `WeChatIPDirectCN.list` as DIRECT; its USP-only
  routing, six removed infrastructure exceptions, DNS and MITM stay intact.
  Canonical Clash imports the same explicit top-level ASN rule after Proxy
  and WeChatIPDirectCN. This intentionally covers other Tencent services in
  AS132203; it is not a claim that the ASN is WeChat-exclusive. Mihomo uses
  ASN.mmdb for this rule. Unreviewed third-party ASN rows stay filtered.

- Additional owner-requested cross-check on 2026-10-25:
  `https://raw.githubusercontent.com/LceAn/proxy-filter-rules/main/rules/WeChat.qx.list`
  (SHA256 `7d5349fecabf5d1289b92e3ebd60103bb54569715291b58e7dd6cdfb317d5ce4`).
  All 40 domain entries and 9 IPv4 /32 entries already match DIRECT; both
  WeChat USER-AGENT patterns are covered by WeChatCore. No new addresses
  are needed. Its AS132203 entry remains excluded as broad Tencent coverage.
  Quantumult X HOST/HOST-SUFFIX and trailing policy labels are not copied
  into SR or Mihomo provider syntax.

- On 2026-10-25, CN adds `WeChatIPDirectCN.list` after Proxy and before
  GEOIP/FINAL: 207 IPv4 and 64 IPv6 rules, converted from the reviewed
  [WeChat snapshot](https://yfamilys.com/rule/WeChat.list), SHA256
  `5beb9891d017ceb6ccbd23dddd7d16bb96c64cb84c6af6749aeb4f1dbd53fa3c`.
  Numeric domain keywords become /24 CIDRs; exact-union aggregation does not
  widen them. Fourteen ranges already covered by CN DIRECT are omitted.
  Owner connection/DNS evidence adds 43.160.144.0/24 and 43.156.255.0/24.
  AS132203 is excluded because Tencent Cloud is broader than WeChat. Shared
  domains remain in existing lists. OS/CNR and their WeChat lists are unchanged.
  The separate CN snapshot intentionally shares some CIDRs with the OS-only
  legacy WeChat list; neither profile loads both IP lists. Canonical Mihomo
  removes the legacy WeChat provider, uses this new list via the filtered
  owner endpoint, and retains WeChatCore with unique translated process rules.

- On 2026-10-21, created owner-maintained `OKX.list` for CN and canonical
  Clash, routed to the existing USP US Reality node before broad lists.
  Official OKX API docs cover `okx.com` (including regional APIs, WebSocket,
  Web3 and static subdomains); the official rename announcement establishes
  legacy `okex.com`; OKX Wallet help links `oklink.com` for transaction lookup.
  Current DNS resolves `www.okx.com` via `awscn.okpool.top`; the owner's earlier
  SR log also exposed `www.okx.com.cdn.cloudflare.net`. Only those exact CDN
  aliases are included, never shared CDN roots or address ranges.
  Removed CN's broad `okx` keyword JP rule. Canonical Clash removes its stale
  keyword/third-party OKX JP route and reuses this owner list at US Reality.
  Crypto.com explicitly remains JP; OS, CNR and all other routing are unchanged.

- On 2026-09-23, OS imported the same owner-maintained `USAI.list` as DIRECT
  and removed its older Anthropic/Claude JP exceptions. OpenAI, ChatGPT, Codex,
  Anthropic and Claude therefore stay DIRECT in OS without copying service
  roots into the profile. CN continues to assign this list to US.
- On 2026-09-23, moved the OpenAI/ChatGPT/Codex and Anthropic/Claude roots
  from `JPServices` into the dedicated `USAI.list`. CN imports this provider
  immediately after `USDownloads`, before `JPServices`, and the redundant
  `DOMAIN-KEYWORD,claude` JP rule was removed. This preserves a single owner
  for each AI suffix and makes the same policy translatable to canonical
  Clash without copying individual domain rules.
- On 2026-09-22, created the shared `TencentMeeting.list` after the latest CN
  export showed 116/117 named meeting connections DIRECT but
  `report.voovmeeting.com` falling to JP. Tencent's current firewall guide
  identifies the whole `*.voovmeeting.com` root as required VooV signaling,
  proxy, resource and reporting traffic. Seven raw Aceville/Tencent media IPs
  were also observed at the same meeting startup; two matching published media
  ranges use their official /24, while the remaining addresses stay exact /32
  to avoid routing unrelated Tencent Cloud space DIRECT. CN and OS import this
  narrow list before regional/broad rules. The same export exposed eight raw
  IPv6 connections as JP, but their qqlive user agents prove Tencent Video
  rather than Meeting; exact /128 entries were added to `TencentVideo.list` so
  CN remains DIRECT and OS preserves its existing CN-media policy.
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
