# YouTube Original Diagnostic v5 — repair still unresolved

This remains an adaptation of the original [Yfamily module](https://yfamilys.com/module/YouTubeAd.sgmodule) and the [Maasea response script](https://raw.githubusercontent.com/Maasea/sgmodule/master/Script/Youtube/youtube.response.js). Both current sources were downloaded again and compared byte-for-byte with the baseline; neither changed. v5 is a bounded diagnostic version, **not a verified ad-removal repair or permanent guarantee**.

## Why this revision

A native client retest confirmed that the v4 additional initplayback empty-response rewrite matched, yet playback advertising remained. That attempted compatibility fallback did not solve the reported issue. It is removed here rather than extended to more playback transports. Restore exactly the original two UDP rules, five URL rewrites, MITM scope and eight response endpoint families; retain the finite limits and existing v3 filtering/enhancement algorithms.

The new capture contains a get_watch result with zero known-player ad-field removals, and other completed get_watch executions without a processing-stage counter. The previous entry guard silently returned on empty, oversize or error responses. Completion alone cannot distinguish those cases. The capture contains no response payload, so the missing structure/reason cannot be established by inventing new protobuf fields or by repeating fixture tests.

## What v5 changes

- Add entry and pass counters for recognized endpoints: input length, normalized HTTP status, body representation and a fixed bypass reason.
- Add read-only player/get_watch counters for known message structure and known ad-field occurrences. Do not print unknown field numbers, field lengths, any values, URL, query, identifiers, account headers, tokens, keys or raw exceptions. The probe is limited to 2048 field headers and 32 known-message expansions and performs no network request, state write or body mutation. An unavailable probe must not affect filtering.
- Normalize HTTP status strings as well as numeric status codes so error responses pass unchanged. This is a guard-correctness improvement, not the proven explanation of current ads.
- Use an immutable version-named v5 script. Do not increase body caps, add new ad-block selectors, block normal videoplayback/SABR or forward traffic to an external Worker.

The original algorithm can filter only the structures it recognizes. Blocking ad measurement requests is not equivalent to removing the delivered advertisement. Synthetic regressions validate scope and output preservation, not the actual account's current advertising payload.

## Next native evidence

Update only this module, title `Original Diagnostic v5`; disable duplicate YouTube modules. Update external scripts and wait for download completion, fully close YouTube, reconnect SR once, then open a new video and reproduce one advertisement. Send the corresponding short PacketTunnel log. The fixed counters identify whether the player response passed empty/status/size gates and whether the known embedded-player schema exists; no raw account response export is requested.

Normal playback/seek, PiP/background and ad removal are separate native acceptance items and remain unverified. If this module affects playback, disable it or restore the [previous original-scope v3 module](https://raw.githubusercontent.com/kenrickxu/SR/b1fdae45c991248360e1b2db2f4578f46288cb45/modules/YouTubeAd.sgmodule). Do not reset CN or change nodes. No CN/rules/node/certificate/service/scheduler changes are made.

## History

Previous v4 compatibility candidate: commit `007eeb35da1031d3b770153b40c03b226a2f6179`; native ad-removal retest failed. v3: commit `b1fdae45c991248360e1b2db2f4578f46288cb45`; active script and feed sanitation confirmed, playback advertising remained. Earlier script versions and exact historical documentation remain in repository history; they are not additional modules to enable alongside this one.
