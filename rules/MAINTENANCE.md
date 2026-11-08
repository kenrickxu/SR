# Ken SR three-family maintenance

Authorized by Ken, SR Topic194 message1365, 2026-11-06. Supersedes earlier manual-only/no-scheduler notes for these three data families only.

## LAN subscriptions removed — owner instruction 2026-11-07, Topic194 msg2252

CN.conf and CNR.conf no longer reference Lan.list. The managed Clash subscription must omit LanDirect and its LanClash.list provider. Do not reattach them during maintenance. Keep the existing SR Skip Proxy/TUN settings, CNR management DIRECT exceptions and US/JP/mainland ordering. Later owner msg2265 requires Clash rules to follow CN.conf exactly (only syntax/provider-name translations), without injecting local-name/private-CIDR DIRECT compatibility rules; remove those extra rows and do not restore them. Clash DNS/TUN/nodes are not synchronized from SR General. LAN mirror files and provenance may remain as standalone source artifacts, not active subscriptions. Existing daily source checks and failure monitoring are unchanged; a mirror refresh must never restore the removed profile references. This overrides older instructions below that describe LAN as an attached provider. CN Skip Proxy follows the exact 12-entry list corrected to star wildcards in msg2092; do not restore old *.lan/ICBC extras.

## CN download-domain migration — Ken Topic194 msg2434, 2026-11-08

CN update-url and its three RULE-SET download URLs now use https://sr-config.kt7766.org (CN.conf plus rules/USProxy.list, rules/JPProxy.list, rules/ChinaDirectDomains.list). This is a fixed-path Cloudflare Worker that returns original GitHub main bytes, never a redirect/open proxy. GitHub remains the only authoritative source. Preserve these CN URLs during maintenance; CNR/OS and native Clash provider URLs remain unchanged. JPProxy already contains DOMAIN-SUFFIX,kt7766.org; add no duplicate routing rule. The importer recognizes ONLY these three exact CN source aliases and retains canonical native provider URLs and pinned-source hash/count checks.

The fifth Worker path /geoip/Country.mmdb serves this repository's existing GeoIP2-CN mirror byte-for-byte (mainland-only). It is an MMDB, not a rule set, and SR selects its URL in Settings -> GeoLite2 database -> Country. CN profile does not define that global client setting; the owner must manually set the new database URL. Do not invent a General key, claim client activation, or replace a global-country database without the owner's intended scope. Owner expressly requested this GitHub mirror in the msg2434 follow-up. Keep the existing daily reviewed mirror/data workflow; never restore old CN raw URLs, game routes, LAN subscriptions or extra native compatibility rows. No paid Cloudflare plan or new maintenance schedule was authorized.

## CN IPv6 link-local exclusion — Ken Topic194 msg2641, 2026-11-08

CN-only tun-excluded-routes now retains the exact14 owner-approved special-use entries and appends only fe80::/10 (15 total). Preserve this explicit IPv6 link-local exclusion during maintenance; it supersedes earlier14-only CN preservation wording. Keep ipv6=false, prefer-ipv6=false, Skip Proxy, DNS, Rule order, nodes, MITM and download URLs unchanged. Do not restore LAN subscriptions, add Apple-domain DIRECT rules or copy this SR-only input exception into CNR/OS/native Clash TUN/rules. The JP importer accepts the exact new15-set while retaining strict extra/subset/duplicate/broader-route rejection and prior approved rollback sets. Native Clash output does not change, so no apply/restart is required solely for this source-only exclusion. This is an owner-authorized compatibility experiment, not a proven AirDrop fix; client reload/reconnect and AirDrop testing remain necessary. No scheduler or client-global tunnel flags changed.

## Reviewed GPT / Telegram supplemental sources — Ken Topic194 msg2677, 2026-11-08

Add https://yfamilys.com/rule/ChatGPT.list to reviewed USProxy inputs and https://yfamilys.com/rule/Telegram.list to reviewed JPProxy inputs. They are NOT new client rule-set subscriptions. Existing owner-hosted lists, US-before-JP order, CN kt7766 download URLs, CNR management DIRECT and CNR mapping of both shared lists to US remain unchanged. Preserve CN/CNR/OS bytes and all unrelated settings. IPv6 list selectors do not enable IPv6. Strict regional provider validation also supports IP-CIDR6 and valid numeric IP-ASN,no-resolve; never ignore unsupported rows.

The existing 03:00 Asia/Hong_Kong job now checks the original eight sources PLUS these two (ten total); do not replace/skip any original source. Preserve 03:35 failure-only monitoring and normal silent success. From business date 2026-11-09, a success receipt requires checked_links=10, existing three successful families, and proxy_sources={chatgpt:ok,telegram:ok}. Earlier business dates retain their original eight-source contract; never rewrite a historical receipt as ten checks. A failed source/partial check or required apply/validation failure must not be marked successful.

Read ProxyServices.review.json before future reviews: it records each candidate decision, exact snapshot hashes, accepted additions, covered rows, held entries and corroboration. Compare upstream additions AND removals against that snapshot; never automatically remove pre-existing owner selectors or promote held rows. Deduplicate exact rows, suffix/keyword coverage and IPv4/IPv6 containment within reviewed inputs; existing owner rows are retained, not globally rewritten. Current ASN ownership corroboration does not replace deterministic CIDRs because client ASN database freshness varies. Re-check ASN ownership and address coverage before changes. Telegram source marker, unrelated/unverified cloud IPs and overbroad GPT shared vendor roots/keyword are held. Keep the broad existing sentry.io JP rule; only verified OpenAI telemetry hosts go US. Do not redirect all Stripe/Auth0/Algolia/Cloudflare telemetry to US.

Source pages expose no explicit redistribution license: do not claim a licensed bulk mirror; use them as candidate facts and corroborate with cited primary service docs, service-list maintainers and RIPE records. Changed terms/unverifiable candidates are held with reasons. Publish only useful semantic deltas with a fresh-main non-force commit, native provider parsing, JP manager review/apply when provider data changes, and actual authorized local/public subscription verification. No changes means no commit/restart. Profiles remain attached only to the same three owner providers; do not restore LAN/game rules or modify TUN/DNS/nodes.

## Schedule and scope

OpenClaw native automation: every day `0 3 * * *`, `Asia/Hong_Kong` (UTC+8, not the host's Tokyo timezone). Sources and review roles are in `MaintenanceSources.json`. Inspect actual data-file commits and content, not repository pushed_at. Clients always use Ken-hosted URLs and Ken refreshes them manually.

- Primary mainland IP: Hackl0us/GeoIP2-CN release Country.mmdb, copied byte-for-byte with provenance/license and reader validation. This remains a hosted download; DO NOT switch SR/Clash database settings. Compare gaoyifan and chnroutes2 as active independent-route references, not blind unions. Do not concatenate MMDBs. A registration or ASN country alone is not verified physical mainland location. Unverified changes are held, not added.
- Primary mainland domains: Loyalsoldier/clash-rules direct.txt. Convert exact/suffix semantics using tools/sync_china_direct.py; use MetaCubeX CN as a complementary candidate source (it integrates ChinaMax, so not an independent second vote).
- Primary LAN: blackmatrix7 Shadowrocket Lan/Lan.list; generate Lan.list and LanClash.list via tools/sync_lan.py. Compare Loyalsoldier private.txt/lancidr.txt for genuine useful additions; these change slowly, daily builds alone are no benefit.

## Required review before publication

1. Read live main, all three provenance files, local additions, and current JP manifest. Pin upstream data-file revisions; fetch bounded content, verify format/size/license and source hashes. No fresh dependency installation is required for an unchanged check.
2. Compare content/coverage, not just timestamps or CIDR row counts. If a new build has identical semantic rules/identical database bytes, do not publish metadata-only noise. Review upstream additions AND removals.
3. Deduplicate normalized exact rows and semantic suffix/IP coverage. Do not broaden exact hosts to parent suffixes. Exclude bare public suffixes such as `.ms`, malformed roots, unrelated shared CDN/platform roots, foreign services accidentally classified by DNS acceleration, and anything justified solely by a larger list. For a new supplemental domain require credible service ownership/use evidence that matches the approved mainland/local purpose; same-lineage agreement is not independent proof. For supplemental IP require concrete mainland-serving/routing corroboration beyond a registration label. Otherwise retain as a candidate and explain why held.
4. Protect JPProxy/USProxy and their precedence, CNR management isolation, all unrelated General/DNS/TUN/MITM/Host/node credentials, OS, IPv6 switch and client state. Do not re-add owner-deleted localhost/local/lan Rule rows. A primary may include special/private ranges: do not relabel them as actual LAN addressing or enable IPv6.
5. `ChinaDirectDomains.local.list` contains the owner-approved `IP-CIDR,100.64.0.0/10,no-resolve` exception. Preserve it across regeneration; this shared/Tailscale range is NOT geographically CN. It deliberately overlaps earlier LAN DIRECT, so effective routing is unchanged. Add no other IP to this list without a new explicit owner request. Keep CN/CNR `skip-proxy`'s `*.lan` addition. Supplemental reviewed domain entries, if any, may be stored in the local input only with per-entry source/reason/date; never replace owner exceptions with upstream data.
6. Stop publication on suspicious mass change, unknown syntax, invalid IPs, changed license, lost source provenance, or failing validations. Investigate within scope; never weaken validators to make a candidate pass. A normal successful upstream rebuild is not evidence a new region is correct. If >1% mainland domains, >5% LAN rows or substantial IP-address coverage is changing, perform explicit deeper checks and hold unresolved changes.

## Supported generation and publication

Work in a private fresh directory on `/srv/storage`, not an old project snapshot. Fetch raw files at live commit; GitHub Contents API may omit >1MB content, so use pinned raw/blob downloads for the domain list. Existing scripts generate candidates only, never deploy themselves.

```
python3 tools/sync_china_direct.py --root CHECKOUT --revision REVIEWED_SOURCE_SHA --input PINNED_DIRECT_FILE
python3 tools/sync_lan.py --root CHECKOUT --revision REVIEWED_SOURCE_SHA --input PINNED_LAN_FILE
```

Read each script first. Preserve local inputs, metadata/hash counts and source licenses. Update ChinaDirectDomains.overrides.json when domain overlap actually changes. A new supplemental LAN entry needs documented provenance, paired exact SR/Mihomo semantics and metadata hashes; do not bolt a raw unreviewed source onto clients. Maintain existing source policy. Reuse maintained readers/builders rather than inventing MMDB encoding. A parser is available at workspace `projects/sr-geoip-cn-mirror/.deps` for bounded validation; reference existing receipt format and queries.

Publish changed files only in one non-force GitHub tree/commit, based on fresh main; check the ref immediately before updating and abort/rebase on concurrency. Preserve all unrelated files. Source success is separate from consumer acceptance. Verify current public raw bytes/counts/hashes. If no effective changes, no commit or service restart.

JP supported manager path: `/usr/local/libexec/hermes-vpn-profile-manager`. Existing SSH access is documented in the private workspace runbook, not in this public repository.

```
hermes-vpn-profile-manager review cn PUBLISHED_SHA
hermes-vpn-profile-manager apply cn PUBLISHED_SHA REVIEWED_PLAN_SHA256
```

Use the returned plan hash, require ok=true, no ignored rules and the existing china-direct-proxy-v1 order/providers. Dynamic provider counts must match reviewed metadata; do not hard-code last month's count. Apply provides native configuration/compatibility validation and managed-manifest rollback. Verify local/public authorized Clash subscription output without printing/storing credentials. Native provider loading must accept the complete changed lists and custom IPv4 row. No VPN/host/client restart; only the existing jp-api transaction restart if needed. MMDB-only data changes without CN/provider changes do not justify applying a different profile or altering DB settings.

## Recording and delivery

Record checked source versions, semantic additions/removals, rejected candidates and reasons, published SHA, validation/apply receipt and any unresolved block in the automation scratch/run result. No cron logs containing account/subscription credentials. No user action is needed until they choose to refresh. No-change runs remain silent; do not create extra schedules or post to unrelated recipients. Preserve failure evidence; do not claim a held/failed update was published or a client has already accepted it.
