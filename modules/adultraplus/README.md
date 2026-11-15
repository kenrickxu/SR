# AdUltraPlus Ken v1

Module: https://sr-config.kt7766.org/modules/AdUltraPlus.sgmodule

Based on https://yfamilys.com/module/adultraplus.module, retrieved2026-11-15. Original attribution retained. This is a full fusion-module adaptation, not a lightweight or all-app-tested build. Replace the original UltraPlus module, do not stack them. Keep the independently accepted YouTube v6 module as-is. CN and regional routing lists are not edited.

## Scoped changes
Remove the Temu whole-domain rejection and three Apple Safe Browsing rejection rows. Add precise Meituan bizad image filtering accepting the observed numeric resize prefix and webp suffix, plus splash-only startpicture/openscreen endpoints with version/query boundaries. Do not block whole Meituan/CDN domains, general appstatus responses, menus, product/shop images, payment or orders. All unrelated upstream Rule, Rewrite, Body Rewrite, Script and MITM entries are retained; the broad upstream MITM scope and other upstream risks are not comprehensively audited or eliminated.

## Evidence and limits
A private44934-line native capture shows the fusion module becoming active at22:50. At22:51:31 both Meituan Takeaway startpicture and openscreen requests were already REJECT-DICT; adding identical rules alone cannot explain or fix all residual ads. At22:53:24 a /0.345.100/bizad/...png.webp asset passed existing prefix-sensitive rules; this candidate closes that observed selector gap. The capture does not prove this asset is the exact splash shown to the owner. Previously cached ad assets, main Meituan app and future ad schemas remain unverified. Do not describe source/selector tests as a permanent app repair.

External scripts retain the original third-party URLs and update behavior (124 distinct dependencies at intake); only the module is mirrored here. They have not all been downloaded or independently audited. No script bodies or user requests are executed/replayed during migration. Native module parsing, individual App behavior, RAM and all script downloads remain phone acceptance items.

Update/import this module, disable the original UltraPlus/overlapping ad-fusion modules, apply, fully exit the affected Meituan App and reconnect SR once. Test main Meituan and Meituan Takeaway separately, including home/shop images, order and payment navigation without submitting payments. Existing cached splash data may survive a reconnect; do not reset all app data. If normal behavior breaks, disable this one module; CN and YouTube remain unchanged.

## Ken v2 correction — 2026-11-15

The v1 claim about preserving general appstatus did not account for an inherited rule: appstatus?ad also matches the ordinary ad_personalized_switch parameter. The native client returned REJECT-200 for that configuration request three times. Remove the appstatus and loadInfo alternatives from that blanket rule, and loadInfo from the other v7 rejection. Keep dedicated startpicture/openscreen rejection and the v1 bizad selector. Add a bounded response-only script for www/wmapi appstatus and loadInfo: empty only nonempty arrays at data.startpicture.ad and .mk, based on blackmatrix7 startup.js known schema. Preserve unknown schema and non-ad fields; parse/status/size failures return the untouched response. The appstatus response body is not present in the capture, so schema applicability and splash removal are not established. No claim of permanent success or confirmed cache causality.

The new script is in this repository, pinned to an immutable commit URL; the module subscription URL stays on kt7766. Existing 124 third-party dependencies retain their original URLs. The additional script uses no HTTP client, storage or raw account/body logging; diagnostic output is a fixed reason and removal count only. Native response buffering and actual memory remain client acceptance items. Finite 1MiB response cap; this is not a further blanket increase to avoid known skip evidence.

Known-schema fixtures and scoped rewrite negative cases passed; no real authenticated requests were replayed. User must retest the splash and normal shop/order navigation. Roll back by disabling this module, or pin the previous v1 module at commit 0cdaf9aaa924412137cba06d8a79e8b4aed106af.

## Ken v3 Diagnostic
This is an evidence-gathering release, not a verified splash-ad repair. The known-schema cleaning behavior and all URL/Rule/MITM ranges are unchanged from v2. New versioned, immutable script adds bounded JSON shape counters: root/data types, code absent/zero/nonzero classification, and aggregate occurrence counts for a fixed allowlist of known ad container names. No request URLs, identifiers, headers, values, unknown key names, exceptions, storage or forwarding are logged. Traversal is bounded to 1024 object/array nodes and depth 8, within the existing 1 MiB client buffer cap. No JSON payloads are exported.
A zero removal count means no cleaning occurred, not that the response contains no advertising. The remaining full-screen ad may originate from existing local material or an unobserved transport; neither is established by the capture alone. Do not block product icons or the whole shared CDN. Phone acceptance remains pending.
