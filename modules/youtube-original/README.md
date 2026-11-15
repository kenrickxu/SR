# YouTube Original Optimized v6 — observed large-player bypass corrected

Based on the original [Yfamily module](https://yfamilys.com/module/YouTubeAd.sgmodule) and [Maasea response script](https://raw.githubusercontent.com/Maasea/sgmodule/master/Script/Youtube/youtube.response.js). Keep the original two UDP rules, five URL rewrites, MITM scope and all eight response endpoint families. Do not enable this alongside Yfamily/Lite/other copies.

## Confirmed difference from the original

The original uses one response script and unlimited `max-size=-1`. This adaptation split handlers and added finite entry guards. Native v5 diagnostics now prove that the added 512KiB playback guard passed three get_watch responses of 2,096,259, 1,676,277 and 2,552,457 bytes through without filtering. That guard is an introduced regression, not a client-update mistake. Earlier absence of a native size-skip notice did not rule out the JavaScript guard. v5 was diagnostic, not a completed ad repair.

The custom low-allocation feed/player filtering and immutable script bundling also differ from the original algorithm. The original Rule, URL Rewrite and MITM sections are preserved exactly here; the unsuccessful extra v4 initplayback fallback remains removed. The original and referenced upstream were re-downloaded and byte-verified unchanged in the preceding review.

## v6 correction

Player/get_watch binary input up to **4MiB** now receives selective wire sanitation. Above **512KiB**, remove only known player adPlacements/adSlots and known embedded recommendation advertisements using the bounded wire walker; do **not** decode the complete response into the upstream object tree or run large JSON.parse. Preserve normal and unknown wire bytes. Inputs above4MiB, large JSON and unsupported/malformed data still pass unchanged with diagnostics. Field/depth budgets remain finite. This is not a measured iOS memory ceiling.

Small playback responses retain existing enhancement/PiP/background handling. Large playback responses preserve whatever features are already present but do not newly apply the full-decoder PiP/background enhancements. Existing feed/control caps stay1MiB/128KiB. No new advertising selectors or blanket videoplayback/SABR/CDN blocks are added. Unknown/future advertising schemas are not guaranteed covered.

Tests use valid ad-bearing protobuf and large opaque normal data at each exact observed byte length, independently decoded with the original schema. The v5 size bypass is reproduced first; v6 removes known ad fields and retains normal data. A decoder-entry tripwire confirms that the large path does not enter full object decoding. These fixtures are not the user's response payload and do not prove real phone playback, memory or complete advertising acceptance.

## kt7766 delivery

Module: https://sr-config.kt7766.org/modules/YouTubeAd.sgmodule

Version-named script: https://sr-config.kt7766.org/modules/youtube-original/youtube.response.v6.js

Both use the existing owner download Worker with only those two exact new public paths. Fixed GitHub repository/main origin, no-store delivery, method restrictions and no client headers/query forwarding remain. v6 script filename is version-frozen; provenance records its origin commit/hash. No credentials, signed media URL, body or key is forwarded to a playback Worker. CN subscription, routing sets, nodes, certificates and schedulers are unchanged.

## Client acceptance

Replace/update the module using the kt7766 URL, enable only this copy, update external scripts and wait for completion, then fully close YouTube and reconnect SR once. Test a new video, at least60seconds of normal playback/seek, advertising, and PiP/background separately. Module title and console counters identify v6. Source/download/fixture checks are not native acceptance. If loading fails, disable this module; historical original-scope v5 is preserved in Git history. No permanent-effect guarantee is made because delivery protocols and schemas can change.

## History

v5 diagnostic commit ddcc0955b07edf0c2c565e219c293cc6a39b299e identified the size bypass. v4 transport fallback was observed to hit while advertising remained, and was removed. Earlier source versions/documentation remain in repository history and are not duplicate modules to enable.
