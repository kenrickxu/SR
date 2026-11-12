# Canonical Shadowrocket CN is Lite

Ken promoted Lite to the existing main CN entry in Topic194 message5437, 2026-11-12 HKT, after the independent trial in message5423.

Use the existing `https://sr-config.kt7766.org/CN.conf`; update the complete profile, apply and reconnect. No new node URL is required. `CN-Lite.conf` remains a compatibility alias, differing only in its self-update URL. Do not automatically switch any running client or apply this SR-only reduction to Windows/Clash.

The canonical profile omits the110190-rule ChinaDirectDomains provider, retaining274 reviewed common-domain selectors plus the original100.64/10 exception, GEOIP CN DIRECT and JP fallback. Current1093 TUN/871 real-IP/1958 Skip are unchanged, as are MY/US/JP/Apple ordering,13 observed UDP media targets and existing DNS/MITM/IPv6/node settings. Unlisted domestic services on overseas addresses may use proxy. Input text is roughly94KB including the four small providers, not a measured RAM reduction; unchanged MMDB/client modules are excluded from that size.

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
