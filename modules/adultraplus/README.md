# AdUltraPlus Ken v1

Module: https://sr-config.kt7766.org/modules/AdUltraPlus.sgmodule

Based on https://yfamilys.com/module/adultraplus.module, retrieved2026-11-15. Original attribution retained. This is a full fusion-module adaptation, not a lightweight or all-app-tested build. Replace the original UltraPlus module, do not stack them. Keep the independently accepted YouTube v6 module as-is. CN and regional routing lists are not edited.

## Scoped changes
Remove the Temu whole-domain rejection and three Apple Safe Browsing rejection rows. Add precise Meituan bizad image filtering accepting the observed numeric resize prefix and webp suffix, plus splash-only startpicture/openscreen endpoints with version/query boundaries. Do not block whole Meituan/CDN domains, general appstatus responses, menus, product/shop images, payment or orders. All unrelated upstream Rule, Rewrite, Body Rewrite, Script and MITM entries are retained; the broad upstream MITM scope and other upstream risks are not comprehensively audited or eliminated.

## Evidence and limits
A private44934-line native capture shows the fusion module becoming active at22:50. At22:51:31 both Meituan Takeaway startpicture and openscreen requests were already REJECT-DICT; adding identical rules alone cannot explain or fix all residual ads. At22:53:24 a /0.345.100/bizad/...png.webp asset passed existing prefix-sensitive rules; this candidate closes that observed selector gap. The capture does not prove this asset is the exact splash shown to the owner. Previously cached ad assets, main Meituan app and future ad schemas remain unverified. Do not describe source/selector tests as a permanent app repair.

External scripts retain the original third-party URLs and update behavior (124 distinct dependencies at intake); only the module is mirrored here. They have not all been downloaded or independently audited. No script bodies or user requests are executed/replayed during migration. Native module parsing, individual App behavior, RAM and all script downloads remain phone acceptance items.

Update/import this module, disable the original UltraPlus/overlapping ad-fusion modules, apply, fully exit the affected Meituan App and reconnect SR once. Test main Meituan and Meituan Takeaway separately, including home/shop images, order and payment navigation without submitting payments. Existing cached splash data may survive a reconnect; do not reset all app data. If normal behavior breaks, disable this one module; CN and YouTube remain unchanged.
