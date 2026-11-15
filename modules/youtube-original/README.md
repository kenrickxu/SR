# YouTube Original Optimized v3 — Shadowrocket

Owner-requested repair of the original Yfamily/Maasea module. Preserve original two UDP rules, five rewrites, complete MITM hostname scope and all eight endpoint families. No CN, routing, node, service or scheduler changes. Historical Lite/v1/v2 scripts remain preserved, not enabled in parallel. See provenance.json for source hashes, scope and immutable script pin.

## Native evidence and remaining uncertainty

The v2 phone retest still contains is_ad=1 advertising playback. Three handlers and a later v2-script download response are present; there is no new max-size skip or critical-memory event in this short capture. The first advertising progress record predates the script download receipt. Handler counts do not establish which cached bytes executed before download, and script-completed does not prove ads were removed. Raw response bodies are not in this capture, so nested/format handling gaps are implementation findings, not a proven exclusive explanation of every ad.

## v3 changes

Use a distinct youtube.response.v3.js filename and immutable repository URL to separate script-name caches. Bounded console counters contain only version, endpoint, input byte length, stage, number removed and detected format. Never log URL/video IDs/account headers/query strings/keys/body content. Whether a client forwards these counters to its PacketTunnel export remains unverified.

Extend the existing schema-limited wire cleaner to player/get_watch, including embedded player adPlacements7/adSlots68 and embedded next recommendations. Preserve normal/unknown bytes. Patch only the upstream entrypoint to consume cleaned bytes and retain sanitized output if subsequent PiP/background enhancement fails; keep successful binary enhancement algorithms unchanged. Detect JSON player/get_watch separately and remove only explicit adPlacements/adSlots/playerAds keys with normal fields retained. Malformed/budget-exceeded input passes original unchanged. JSON branch adds ad-field handling, not a new PiP/background promise.

Keep v2 browse/next/search low-allocation traversal, finite input limits (feed1MiB/playback512KiB/controls128KiB), and field/depth budgets. Limits are not a measured RAM ceiling. Do not blanket-block videoplayback/SABR or advertiser domains, introduce third-party playback forwarding, or assert unknown future/server-stitched ads are covered.

## Acceptance and rollback

Update this module only, disable Yfamily/Lite/duplicates, download/update external scripts and wait for completion, confirm v3, completely close YouTube and reconnect SR once before opening a fresh video rather than continuing an already playing/cached ad. Verify advertising, normal play/seek for at least60seconds and PiP/background separately. Actual native parsing/ad removal/playback/RAM remain phone retest items.

Synthetic tests use the original upstream protobuf decoder independently: nested mixed normal/ad get_watch, player ad fields, enhancement-error cleaned fallback, Unicode JSON, malformed fail-open, preserved binary PiP/background and anonymous diagnostic counters. They do not reproduce real account payloads or prove actual phone repair.

Rollback: commit e24c9023a39ffd190dc10d88e6c4eaaf1613caca modules/YouTubeAd.sgmodule. Private captures stay in the owning private project and must not be published or replayed.
