# YouTube Original Optimized v2 — Shadowrocket

Owner-requested repair of https://yfamilys.com/module/YouTubeAd.sgmodule, retaining Maasea attribution and original playback enhancement. This updates the original-scope module, not the separate historical Lite variant. Exact source hashes/build are in provenance.json.

## Evidence and correction

A phone retest showed Sponsored video advertising. Its native capture recorded a browse response skipped at 133067 > 131072 bytes. The v1 128 KiB feed threshold therefore bypassed a real response. This proves a concrete ad-filter coverage gap, not that it alone accounts for every advertisement. The short retest contained no critical-memory/close-all event; it does not establish long-run memory stability or complete ad removal.

## Changes in v2

Preserve the original two UDP rules, five URL rewrites and full MITM hostname line unchanged. Preserve all eight endpoint families. Split handlers into browse/next/search (1 MiB), player/get_watch (512 KiB), and reel/guide/account controls (128 KiB). All are finite; oversize, unsupported, error and malformed inputs pass unchanged. Limits are input-body thresholds, not a measured RAM ceiling.

For browse/next/search, use selective protobuf wire traversal derived from the copied upstream schema. Follow only known feed/container paths to repeated rich-item cards. Remove cards matching upstream pagead or EML-layout signatures; preserve the upstream Shorts-layout rule. Do not decode the whole feed into a JavaScript object graph. Retained normal/unknown wire fields remain byte-identical, including opaque payloads; changed parent lengths are recomputed. Small matching ad cards no longer have the upstream 1000-byte scan exemption. Do not persist or trust a global safe-field-number cache: the same field can contain both normal and advertising cards. Keep depth/field budgets and fail open on malformed wire data. Unknown future feed shapes/signatures and uninspected endpoint payloads are not claimed covered.

For all other supported endpoints, keep the full upstream implementation verbatim inside the bounded guard, including player ad fields and PiP/background logic. Explicit argument values retain the original effective defaults. No new request redirect/Worker, third-party playback forwarding, broad advertiser-domain block, CN/route/node/subscription service/scheduler change is introduced.

## Accept and roll back

Update/reimport the modules/YouTubeAd.sgmodule subscription, enable only this variant, and disable old Yfamily/Lite/duplicate YouTube modules. Do not reset CN or change JP. Completely close YouTube, apply the module and reconnect SR once, then revisit the previously advertising feed/video and play/seek a normal video for at least 60 seconds. Check PiP/background separately. Phone-native loading, real advertising outcomes, continuous playback and actual RAM remain owner retest items.

Rollback module version: repository commit 7bed51c1ebedde229699f941c1b52da9018e1ff7, modules/YouTubeAd.sgmodule. Rollback does not require changing CN or routing.

Tests use synthetic ads/normal cards and original upstream protobuf types as an independent decoder, including an exact 133067-byte regression fixture. These do not reproduce actual account response payloads or prove all advertising gone. Private screenshots, logs, bearer URLs, cookies and certificates are never included in public files.
