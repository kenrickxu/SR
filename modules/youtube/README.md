# YouTube Playback Lite (Shadowrocket)

Opt-in playback-first adaptation of the owner-supplied https://yfamilys.com/module/YouTubeAd.sgmodule, using Maasea's response script with attribution retained. Not a replacement for CN routing and not enabled automatically.

## Changes and trade-offs

- Keep the original two YouTube-only UDP-reject rules to retain the existing TCP path.
- Remove both googlevideo URL rewrites and all googlevideo MITM hostnames. Video-CDN HTTPS is not decrypted by this module; existing JP routing is untouched.
- Match only exact YouTube player/get_watch response endpoints, not search/browse/next/guide/reel/account responses. Home/search/Shorts ads and other enhancements are intentionally not promised.
- Set a finite max-size of1048576 bytes and a matching fail-open JavaScript body/status/endpoint guard. The wrapper cannot prevent the client from buffering before execution; this is not a measured RAM ceiling or a fix for all memory pressure.
- Resolve all argument placeholders to fixed values: translations off, debug off, UI hiding off. Use default client script engine rather than an unresolved engine template.
- Bundle the exact upstream response script in this repository, pin the module dependency to its immutable commit, and record hashes in provenance.json. Do not auto-follow upstream master.

## Import and one-device acceptance

1. Preserve the old module URL/settings and disable every old/duplicate YouTube ad-blocking module; do not stack this one with the old module.
2. Import modules/YouTubeAd-Lite.sgmodule using its raw GitHub URL. Keep CN and existing JP group selected.
3. Fully close YouTube, reconnect Shadowrocket once, reopen YouTube and play the same video; verify picture and sound for at least60seconds, then seek. Check that critical/close-all recycling does not recur. PiP/background and ad-blocking require separate phone acceptance.
4. Do not enable full HTTP/body debug logging during ordinary playback. For a failing retest, collect a bounded reproduction log and exact test time.
5. Roll back by disabling this module and re-enabling the previously preserved old module; CN and routing do not need a rollback.

This is an experimental scoped mitigation, not a proven complete repair. Existing diagnostics show later memory-critical recycling and video disconnection, but do not prove the cause of the initial loading stall or that one module alone consumed all memory. No signed playback URLs, account headers, certificates or uploaded logs belong in this public directory.
