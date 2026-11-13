# Canonical CN: explicit proxy lists, default DIRECT

## Current canonical SR explicit-proxy/default-DIRECT — Ken5678,2026-11-13 HKT

CanonicalCN/originalURL now follows explicit proxy lists then FINAL,DIRECT. General has NO always-real-ip, exactly12 minimal Skip selectors (user underscores corrected to wildcard stars),14 user-requested special TUN entries including127/8 despite historical iOS invalid-route warning. This explicit mode change supersedes earlier1094/871/1959 coverage-preservation/no127 directives only for SR CN. Do not restore domestic publicTUN/RealIP/Skip growth or full/commonChina/GEOIP direct stages: defaultDIRECT already supplies that policy. Games are played with SR switchedOFF by Ken. Unknown foreign domains and rawIPs not covered by explicit proxy sets nowDIRECT, not auto-country detection. ExistingFakeIP remains, so DIRECT is not fullSR bypass and memory improvement is not measured.

Main6rules: CNMediaDirect exact17UDP targets→MYProxy→USProxy→JPProxy→CNForeignProxy→FINALDIRECT. Existing MY/US/JP source lists/order/groups unchanged. Two new CN-only rule sets use raw-ownedGitHub URLs (no Worker path expansion). CNForeignProxy61rows(54suffix+7precise) derived from observed commonly-used foreign service hosts; no broadAWS/CloudFront/Workers/CDN roots or unrelated ads/unknown probes. US/MY earlier priorities preserved; APNsTCP/domainJP and exactUDP media exceptions remain. AppleDirect data retained unchanged for other consumers but unnecessary broadApple/directDom/GEOIP stage removed fromSR. New unfamiliar foreign services need evidence-backed selectiveJP supplementation, not blanketforeignIP/ASN rules or auto-growing domesticbypass.

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
