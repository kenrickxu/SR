# Independent Shadowrocket CN-Lite

Ken opted into the independent Lite trial in Topic194 message5423, 2026-11-12 HKT. Full `CN.conf` remains the unchanged rollback profile. This file is SR-only; do not apply it to managed Clash, Windows or the independent iPhone Clash subscription.

Import `https://raw.githubusercontent.com/kenrickxu/SR/main/CN-Lite.conf` as a separate profile, select/apply it and reconnect. Keep the existing full CN entry. Existing node subscriptions and MY/US/JP/Apple rule-set URLs remain; no node credentials or DNS/MITM/IPv6 settings are changed by the derivation.

The whole ChinaDirectDomains provider is omitted. A reviewed common-domain subset is inserted at the same DIRECT stage, followed by the original GEOIP CN DIRECT and JP fallback. Unknown mainland services on overseas addresses may use proxy; this is an intentional opt-in coverage tradeoff, not lossless compression. The profile plus referenced text rules total roughly94KB instead of3MB; this excludes the unchanged MMDB and client modules, and is not a measured RAM reduction.

All current TUN exclusions, real-IP and Skip strings are retained exactly. Previously reviewed domestic game IPs remain excluded from TUN, and known game DNS/HTTP exclusions remain. This cannot certify every future game address, application-specific proxy ingress, client override, or actual full-game behavior.

Keep observed FaceTime media UDP exceptions DIRECT ahead of APNs shared-IP fallbacks, and keep TCP/domain Push on JP. DIRECT does not mean bypassing the SR TUN. TUN IP exclusions cannot distinguish UDP media from TCP Push on a shared address: do not add the shared Apple ranges or media addresses to TUN merely to claim full FaceTime bypass. Apple's documented APNs networks overlap the observed media addresses. Full FaceTime audio TUN bypass and all possible bare-IP Push JP cannot both be guaranteed by the current IP-only mechanism. Actual calls and lock-screen notifications require phone verification.

## Rebuild and consistency

From a current candidate checkout containing the authoritative CN and rules:

```
python3 tools/build_cn_lite.py
python3 tools/build_cn_lite.py --check
```

The generator is deterministic, does not fetch sources or apply runtimes, and emits `CN-Lite.conf` plus `CN-Lite.source.json`. Every admitted domain selector is a subset of current full-China domain-DIRECT coverage and originates from the approved General real-IP families, apart from the existing cn suffix and sole100.64/10 exception. Apple-covered domains are not duplicated. This is not a new external source or recurring task.

When an authorized source change affects CN General/rules or any referenced lists, regenerate against the same proposed source revision and include derived files in the same reviewed publication, then verify bytes. Do not restore the full China provider into Lite during daily maintenance, automatically switch full CN users to Lite, or expand domain/TUN scope to make a test pass. Keep current 13 external source checks,03:00/03:35 scheduling and delivery policies unchanged. Full CN/native importer policy and all excluded consumers remain separately guarded.

Rollback is selecting the retained full `CN.conf`; do not blindly replay an old repository or remove later owner changes. Phone memory/behavior comparison must use matching network and app activity, normal versus reproduction logging, and actual installed client version. No claim of preventing OOM without client evidence.
