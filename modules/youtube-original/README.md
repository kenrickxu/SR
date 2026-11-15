# YouTube Original Optimized — Shadowrocket

Owner-requested optimization of https://yfamilys.com/module/YouTubeAd.sgmodule, not the separate Lite variant. Maasea attribution retained; upstream snapshot/hash recorded in provenance.json.

## Preserve the original behavior surface

Keep the original two UDP-reject rules, all five URL rewrite lines (including both googlevideo rewrites), and the complete MITM hostname line byte-for-byte. Keep every original API endpoint family: browse, next, player, search, reel/reel_watch_sequence, guide, account/get_setting and get_watch. Keep the original Maasea implementation verbatim inside an entry guard; do not invent a new ad algorithm or silently upgrade to a different module's additional request scripts.

The old unresolved argument placeholders caused the current upstream parser to retain its defaults. Set known equivalent defaults explicitly: caption translation off, blockUpload=true, blockImmersive=true, blockShorts=false, debug=false; lyric translation off for legacy compatibility. Use the client default engine instead of an unresolved engine placeholder. PiP/background and ad handling logic are retained, not verified business outcomes.

## Bound body processing

Split the original endpoint coverage into disjoint playback and list-response handlers. Limit player/get_watch to524288bytes and browse/next/search/reel/guide/account responses to131072bytes in both module max-size and JavaScript checks. Pass empty, oversized, unrelated or non-success responses unchanged; do not return an empty forged response or truncate protobuf. Small supported payloads execute the exact upstream algorithm. The guard does not prevent all client buffering, script-engine overhead or aggregate memory pressure, and these limits are not a measured RAM ceiling. Oversized responses can retain advertisements/enhancements because stability takes precedence over rewriting every payload.

Pin the copied script to an immutable commit in this repository. Updating this module URL does not silently follow upstream master. No CN/routing/subscription/service/scheduler changes.

## Import, accept, roll back

Disable both the old Yfamily YouTube module and any Lite/duplicate YouTube module. Import the raw modules/YouTubeAd.sgmodule URL and enable only this variant. Keep CN/JP unchanged. Close YouTube, reconnect Shadowrocket once, reopen and play the same video for at least60seconds, seek and check picture/sound. Check homepage/search ad behavior, PiP/background separately. Avoid full HTTP/body recording during normal playback; collect only a bounded reproduction if still failing.

Roll back by disabling this module and re-enabling the preserved original URL. Do not delete or reset CN. Tests prove static scope, guards and synthetic upstream-equivalent execution only; actual Shadowrocket parsing, memory and playback remain unverified until the phone test.

Raw logs, bearer URLs, account headers and certificates must never be copied into this public directory.
