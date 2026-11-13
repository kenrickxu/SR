## Domain simplification — Ken5750/5751, 2026-11-13 HKT

Final current counts: MY32 / US52 / JP302, including242 DOMAIN-SUFFIX domain rows and144 retained IP/ASN rows across allthree sets. All domain selectors in MY/US/JP now DOMAIN-SUFFIX. Merge reviewed first-party manepa.jp/spark-fintech.com siblings and scoped okx.com.cdn.cloudflare.net JP tenant; keep US earlier precise www.okx.com.cdn.cloudflare.net. Existing2048ai.vip parent suffix retained once (includes /media/videos paths/subdomains). Shared cloud/S3/Azure/Workers/Imgix/Sentry tenants stay at known full tenant hostname, never broaden them to platform root solely for shorter text. All non-Apple existing IP/ASN rules retained, as IP-only connections cannot become hostname matches. Domain-selector family coverage retained; broad keyword substring fallback is intentionally narrowed, NOT a lossless infinite-domain rewrite. Known1234 observed connection-host regional decisions checked against post-Push-direct candidate; confirmed service families receive parent suffixes. Keyword-only advertising/telemetry and unverified dependencies are not newly supplemented as proxies and now use normalDIRECT; exact changed hosts recorded in suffix-audit.json. Unobserved unknown names use static fallback. No blind foreign or shared-platform additions. Owner policy override recorded in ProxyServices.review.json; do not reintroduce DOMAIN/DOMAIN-KEYWORD at future maintenance without explicit reason/owner review. MY list hash/count sidecar and exact old/new tenant-type native checks synchronized. Source and native structure remain separate from shared provider data, which consumers obtain on refresh. Actual phone connectivity/Push acceptance pending.

## Current Apple/Push DIRECT-first CN — Ken5746/5748, 2026-11-13 HKT

Ken5746 prefers DIRECT wherever usable; Ken5748 explicitly says Push DIRECT. Current SR CN now has5 executable rules /3 downloaded sets: MYProxy→USProxy→JPProxy→GEOIP,CN,DIRECT→FINAL,DIRECT. Remove exactly11 conflicting JP selectors: push.apple.com suffix, cloudflare.com suffix, five IPv4 +four IPv6 APNs fallback prefixes. JP342→331; all other selectors/options/order retained. No replacement broad DIRECT/proxy exception list. Remove allfive now-redundant inline Apple/media DIRECT rows; no CNMediaDirect reference. Push domains and bare APNs targets now use SR default DIRECT. NonPush Apple/iCloud/FaceTime and two PCC hosts also fall through, not hit prior JP fallbacks. Existing challenges.cloudflare.com exception and cloudflare-dns.com/precise exchange CDN service rules remain; other cloudflare.com subdomains can now DIRECT.

This explicitly supersedes historical Push-JP/domain/TCP-IP-fallback and five-inline-guard requirements only within this change. Do not auto-restore those11 denied JP rules or inline guard layout from old5718/5735/5740 instructions, old owner supplement lists or feeds. ProxyServices.review.json owner_direct_first_5748 is current owner override. No assertion that direct connection from mainland phone or lockscreen notification delivery has been tested: actual acceptance follows manual refresh/reconnect. No automatic direct-first/fallback-on-failure logic is introduced; normal first-match static rules and FINAL DIRECT remain.

General RealIP0/Skip12/TUN14, originalCN URL/alias, MY/US/groups/nodes/DNS/MITM/Host/IPv6 and all other JP rows unchanged. Other clients retain native structural policies and prior routes/RealIP; sharedJP data removal propagates on consumer refresh according their existing rule order, not necessarily same effective default as SR. No managed native/Windows/VPN apply. Strict exact new5/old10/legacy source and General compatibility, negative/rollback/native/actual subscription/newasset/download checks required; only necessary subscriptionAPI compatibility reload. Preserve full/Lite reference archives,13sources/03:00+03:35HKT/delivery/alerts/5487quarantine, declined8-lives-cat.io family, privacy and evidence boundaries. No speculative deletion of other JP services based on foreign-server direct probes.

## Current CN: inline Apple/media guards — Ken5740, 2026-11-13 HKT

Current SR CN uses ten executable rules and only three downloaded sets: five unchanged Apple/media DIRECT selectors inline, then MYProxy → USProxy → JPProxy → GEOIP,CN,DIRECT → FINAL,DIRECT. No CNMediaDirect.list URL or runtime dependency in CN/CN-Lite/source hashes. Its file remains unchanged for historical reference/rollback, not an active maintenance target. Future necessary evidence-backed Apple/media changes belong in these inline rules, not a restored standalone set. This supersedes earlier 5735/5718/5715 wording ONLY on storage/grouping; none of their effective matching is removed.

Keep exact PCC hosts, apple.com AND NOT push.apple.com, icloud.com, and UDP-only nine APNs prefixes in the same order before the three proxy sets. Push domains/TCP fallback remain JP; unknown bare TCP in APNs space can still be JP, not proven exclusively Push. DIRECT is not full SR bypass or phone business acceptance. General remains RealIP omitted / Skip12 / TUN14; no nodes/DNS/MITM/IPv6, game bypass, full China table or foreign-service expansion. JP342 unchanged; declined 8-lives-cat.io family must not be re-added. Preserve other clients' native projection/policies; accept only exact reviewed inline layout and exact General, retain old layouts for rollback, no weakening of negative checks. Only necessary subscription API reload; no VPN/Windows native apply. GitHub sole authority, original CN URL/alias/reference archives,13 sources/quarantine/03:00 and03:35 schedules/delivery/alerts retained.

## Owner removes unnecessary backup exception — Ken5735,2026-11-13 HKT

Remove DOMAIN,api-production.8-lives-cat.io fromJP343→342. Do notauto-readd thisfamily orparentselector aspreviouslyvisitedforeignwebsite: itisautomaticSDKbackend andownerdeclinesitsproxyexception. Original5718evidence remains historical, notcurrentauthority. PrimaryRevenueCatexistingrows unchanged.

Keep CNMediaDirect5rules andmain6/4structure: conditionalrequesttoomit onlyifdefaultDIRECTwouldbesame isnottrue. WithoutthisearlyDIRECTset, apple-relay.cloudflare.com/cp4.cloudflare.com hitcloudflare.com JP, and17.188.171.27UDP3482hits17.188.128/18 JP. JP-before-GEOIP/FINAL defeatsdefaultDIRECT. NoCN/alias/General/media/MYUS/native/runtimechange orAPIreload. Fullstrictreview/download/consumercompatstillrequired;13sources/schedules/alerts/quarantineotherfencesremain.

## Apple/default-DIRECT and history supplement — Ken5718,2026-11-13 HKT

MainCN6rules/4sets andGeneralremainunchanged. JP342→343 adds onlyobserved api-production.8-lives-cat.io, officiallyRevenueCatbackup.29 ownhistoricalanalysisfiles/1234connectionhosts reviewed; no blindforeign/ads/sharedCDNunion. RevenueCatprimaryalreadyJP, thisprecisebackupwasmissing.

CNMediaDirect now5compactrules: exactapple-relay.cloudflare.com/cp4.cloudflare.com DIRECT beforebroadcloudflareJP; knownnonPushapple.com (explicitNOTpush.apple.com) andicloud.com DIRECT beforerawAPNsIPfallthrough; UDP-only9existingAPNsprefixesDIRECT preservesall17previousmediahosts andfutureUDPinthoseprefixes. No17/8bypass/General/TUN/Skip/IPv6change. PushdomainandTCPIPfallbackJP stay;unknownrawTCPinthesharedprefixes cannotbeprovenPush-exclusive, so do notpromiseonlyPushJP/allfutureAppleDIRECT. DIRECTisnotfullSRbypass orcall/notificationacceptance. OtherunmatchedAppleusesFINALDIRECT; do notrestore236rowAppleDirecttable, independentforeignset orlargeChinadataintoSR.

This isCN-onlyApple/media data, whileJPbackupdataissharedonconsumerrefresh. Native/iPhone/Windowsrules intentionallynotapplied; source layoutunchanged/strictformalreview/actualsubscribersstillrequired. Oldexact17-onlymediaclauses supersededonlybyUDPprefixcoverage;TCPPush/nativeprivacy/13sources03:00/03:35/5487quarantine androllbackfencesremain.

## JP supplement consolidation — Ken5715,2026-11-13 HKT

CurrentCN has6rules/4sets: CNMediaDirect→MYProxy→USProxy→JPProxy→GEOIP,CN,DIRECT→FINAL,DIRECT. The previously61-row CNForeignProxy supplement is now merged intoJPProxy (281→342), with alloldselectors/options preserved and domainrows beforeIProws. No newforeign coverage beyond the alreadyapproved61; MY/US remainearlier. CNForeignProxy URL retained as comment-onlydeprecatedstub, notloaded; do notrecreateseparateCNForeignProxy set or importit atmaintenance. JPServices19/otherownerinputs keptuntouched. Review/provenance inProxyServices.review.json owner_jp_supplement_5715; futuredaily sourceupdatesmustpreserve theselocalownerrows andcurrentJPdata, not old281literalcount. ExistingYfamilyquarantine/thirteenfeeds remain.

SharedJPprovider data changes for consumers onrefresh, includingnative/iPhone/CNRaccordingtoexistinggroupmapping; this isnot a runtimeapply orautomatic clientrefresh. Preserve strictold6/old7/newmerged6 sourcecompatibility and GeneralRealIP0/Skip12/TUN14,17media/PushJP,US/MY,nodes/DNS/MITM/IPv6 and defaultDIRECT. OriginalCNURL/GeoIPCNorder/rollbackarchives/03:00+03:35deliveryalerts stay. Older5678/5701separatesupplement/fiveproviderwording below is supersededonlyonthisgrouping.

# Canonical CN: explicit proxy lists, default DIRECT

## GeoIP CN ordering amendment — Ken5701,2026-11-13 HKT

CurrentSRorder is7rules: CNMediaDirect→MYProxy→USProxy→JPProxy→CNForeignProxy→GEOIP,CN,DIRECT→FINAL,DIRECT. Explicitproxyexceptions takeprecedence overcountrymatching. GEOIP CN isrequestedclarity/extensionpoint, not anadditionalproxy/defaultpolicy; unknownforeignstillDIRECT. Itusesclientcountrydatabase, not anewremoteRULE-SET. Fiveproviderlists/General remainunchanged (RealIP0/Skip12/TUN14). This supersedes5678 six-rule/no-GEOIP statements only; do notrestoreoldcompactdomains/largeTUN. Strictold6+new7nativecompat andactualsubscriptionsmustpass. Allother5678safeguards/13sources/schedules/rollback/runtime/privacyremain.

## Current canonical SR explicit-proxy/default-DIRECT — Ken5678,2026-11-13 HKT

CanonicalCN/originalURL now follows explicit proxy lists then FINAL,DIRECT. General has NO always-real-ip, exactly12 minimal Skip selectors (user underscores corrected to wildcard stars),14 user-requested special TUN entries including127/8 despite historical iOS invalid-route warning. This explicit mode change supersedes earlier1094/871/1959 coverage-preservation/no127 directives only for SR CN. Do not restore domestic publicTUN/RealIP/Skip growth or full/commonChina direct stages: defaultDIRECT already supplies that policy. Games are played with SR switchedOFF by Ken. Unknown foreign domains and rawIPs not covered by explicit proxy sets nowDIRECT, not auto-country detection. ExistingFakeIP remains, so DIRECT is not fullSR bypass and memory improvement is not measured.

Prior5678 main6rules: CNMediaDirect exact17UDP targets→MYProxy→USProxy→JPProxy→CNForeignProxy→FINALDIRECT. Existing MY/US/JP source lists/order/groups unchanged. Two new CN-only rule sets use raw-ownedGitHub URLs (no Worker path expansion). CNForeignProxy61rows(54suffix+7precise) derived from observed commonly-used foreign service hosts; no broadAWS/CloudFront/Workers/CDN roots or unrelated ads/unknown probes. US/MY earlier priorities preserved; APNsTCP/domainJP and exactUDP media exceptions remain. AppleDirect data retained unchanged for other consumers but unnecessary broadApple/directDom/GEOIP stage removed fromSR. New unfamiliar foreign services need evidence-backed selectiveJP supplementation, not blanketforeignIP/ASN rules or auto-growing domesticbypass.

Maintain fresh main via tools/build_cn_lite.py and --check, both oldLite and exactnewmode supported. Keep CN-Lite alias samepolicy; CN-Lite-Reference.conf and archive/cn-lite-before-default-direct-20261113-1000bcc/ preserve priorLite, originalCN-Full/frozenfullarchive untouched. NativeWindows/CNR/independentiOSClash routing is explicitly NOT switchedtoDIRECT: strict exactnewSR-source projection maps to retained prior native policy and iOS1094routes/871RealIP baseline, noapply/restart. Source acceptance does not apply SRnewmode to those clients. New source layout must pass raw/native negative/rollback tests, formalmanager0ignored, actual subscriptions and downloads beforepublication; only necessaryAPI module reload allowed.

Retain13external sources/03:00+03:35HKT/reportdelivery/alerts and currentcontrolledYfamilyquarantine. FullChina/GeoIP source maintenance still servesotherconsumers; do not reattach them toSRorclaim13feedsretired. NoDNS/IPv6/MITM/Host/nodechanges;127acceptance/notification/call/RAMand unknownsites remainphoneverification.


Historical layout details below refer to the prior Lite reference, not current main.

# Canonical Shadowrocket CN is Lite

Ken promoted Lite to the existing main CN entry in Topic194 message5437, 2026-11-12 HKT, after the independent trial in message5423.

Use the existing `https://sr-config.kt7766.org/CN.conf`; update the complete profile, apply and reconnect. No new node URL is required. `CN-Lite.conf` remains a compatibility alias, differing only in its self-update URL. Do not automatically switch any running client or apply this SR-only reduction to Windows/Clash.

The canonical profile omits the110190-rule ChinaDirectDomains provider, retaining274 reviewed common-domain selectors plus the original100.64/10 exception, GEOIP CN DIRECT and JP fallback. Current1094 TUN/871 real-IP/1959 Skip retain prior coverage, as are MY/US/JP/Apple ordering,17 observed UDP media targets and existing DNS/MITM/IPv6/node settings. Unlisted domestic services on overseas addresses may use proxy. Input text is roughly94KB including the four small providers, not a measured RAM reduction; unchanged MMDB/client modules are excluded from that size.

Known domestic-game IP bypass/DNS/HTTP exclusions are retained, not a guarantee for every future IP or explicit proxy ingress. FaceTime media DIRECT avoids proxy nodes but is not full TUN bypass. Do not add shared Apple/APNs IPs to TUN to claim complete audio bypass: IP routes cannot distinguish UDP media from same-IP TCP Push. Preserve Push domain/TCP JP, and require actual phone calls/lock-screen notifications for runtime acceptance.

## Full-version reference

`CN-Full.conf` is a frozen-reference convenience profile: its five rule URLs are pinned to7106fd49b7b66aea73dafba17e2c3d699899a26f, and its update URL points to itself rather than canonical Lite. The exact unmodified old profile, source metadata, rule data and MMDB are retained under `archive/cn-full-20261112-7106fd4/` with MANIFEST.json size/SHA receipts. This archive is not an active source or daily-maintained full profile. The original archived CN.conf retains its historical update URL; do not auto-update that exact-evidence copy as if it were an independent full subscription.

## Maintenance

Edit current canonical `CN.conf` for authorized changes. Run:

```
python3 tools/build_cn_lite.py
python3 tools/build_cn_lite.py --check
```

The deterministic tool validates the canonical Lite layout and synchronizes CN-Lite alias/source sidecars. It does not rebuild canonical CN from the archived full profile or reattach the large China list. Keep General typed scopes, previous bypass coverage and proxy fences. New Lite DIRECT changes require a source review and the corresponding exact JP/iOS compatibility guard update/test before publication; never relax arbitrary-domain/widening guards to make maintenance pass.

The full ChinaDirectDomains data remains available and maintained for CNR/other native consumers. JP's strict source adapter projects only the exact approved275-row SR-Lite block back to the previous full-provider native layout, without runtime apply; its full-source rollback guards remain. The independent iPhone adapter accepts the same reviewed projection while retaining its existing full MRS/rules behavior. This compatibility is not permission to lighten native consumers or apply Windows policy.

Existing13 external source checks,03:00/03:35 HKT schedules, daily reports and failure alerts remain. Treat earlier independent-only CN-Full-preservation notes as historical; do not restore the full provider into canonical CN. Future rollback must be scoped and fresh-source aware, never a replay of an old repository.
