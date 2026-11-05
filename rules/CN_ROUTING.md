## Owner-hosted LAN list — 2026-11-06

Ken SR Topic194 message1297 requests analysis and owner hosting of
blackmatrix7/ios_rule_script rule/Shadowrocket/Lan/Lan.list. Lan.list keeps
the full reviewed 142 rows:9 exact domains,115 suffixes,18 IP rows including
4 IPv6 ranges. These include router/local-service names, reverse DNS names,
private/shared/link-local and special-use/documentation/multicast/reserved
ranges. 198.18.0.0/15 is benchmark space also used for fake IP; it is not a
real LAN subnet to configure on a router. The list is not a pure RFC1918 list.
Some listed names are public vendor namespaces. Preserve reviewed scope;
do not generalize public vendor roots or manufacture parent domains.

Source revision and SHA256, generated SR/native hashes and counts are kept
in Lan.source.json, GPL-2.0 license in Lan.LICENSE. tools/sync_lan.py manually
fetches the latest upstream commit touching this file and reports additions
AND removals. It only writes repository files, never publishes or schedules.
Clients consume Ken's own GitHub mirror, not the changing upstream URL.

CN/CNR reference Lan.list with DIRECT before USProxy/JPProxy; it replaces
the3 remaining duplicate inline local IPv4 rules127/8,169.254/16,100.64/10.
CNR's five owner-management DIRECT exceptions remain explicit and first.
General skip-proxy and all unrelated settings are unchanged. No inline
localhost/local/lan is restored to SR after the user's earlier removal.

Clash consumes LanClash.list: same142 row meanings with the4 IPv6 IP-CIDR
rows normalized to native IP-CIDR6. IPv6/DNS IPv6 switches remain false;
a rule containing IPv6 or an ip6.arpa domain does not enable IPv6 transport.
Mihomo keeps its existing3 local-name DIRECT protections (SR has no literal
copies) then LanDirect,USProxy,JPProxy,ChinaDirectDomains,GEOIP CN,DIRECT,
MATCH JP. Prior private-CIDR compatibility inlines are omitted only when
LanDirect is present, since this provider covers them. All4 native providers
are classical/text HTTP using the owner mirror and existingJP downloader.
Current counts:CN6 main rules,CNR11,Clash9 main rules/4providers.

Validate source/native exact row conversion and hashes, provider references,
ordering, DNS/TUN/proxies/MITM preservation and actual native parsing/loading.
Publication/provider loading is not phone acceptance. User refreshes selected
CN/CNR configs and referenced lists, or Clash subscription and providers.
Manual list maintenance must review changes to reserved/fake-IP ranges,
public vendor names and IPv6 syntax, not blindly append unknown new types.

## JP/US proxy selectors consolidated — 2026-11-06

Owner SR Topic194 message1264 requests two GitHub proxy classifications.
JPProxy.list holds 253 explicit JP domain/keyword/IPv4 selectors; USProxy.list
holds 28 US selectors. Policy is supplied by the profile reference, not baked
into list rows. CN references USProxy with US REA first, then JPProxy with JP
REA; CNR maps both to US. Existing local/private rules and CNR management
DIRECT isolation remain ahead of these sets. ChinaDirectDomains/GEOIP and
JP-or-US default remain behind them. CN main rules14, CNR19; Clash14 with
three native classical/text HTTP providers.

This grouping establishes US-first precedence across the two complete sets.
Listed root/www hosts and independent IPv4 decisions were checked against the
previous table. It is NOT a claim that every constructed mixed context is
identical: e.g. a host matching JP suffix marscode.com AND US keyword
polymarket, or a JP hostname paired with an explicit US IP, now follows US.
Do not describe grouping as a pure order-preserving expansion of the former
interleaved table. This chosen priority is reported to Ken during rollout.
Within each set original selector order and no-resolve options remain.

For future requested proxy additions, edit the appropriate owner JPProxy.list
(default) or USProxy.list if explicitly requested, check cross-set coverage
and precedence, then synchronize CN/CNR/JP Clash sources and provider/native
outputs. Usually CN/CNR references need no editing if unchanged; update JP
manifest revision as needed to keep authority bookkeeping current. CNR must
retain its owner-management DIRECT prefix. Do not import an owner's omitted
IP into CNR proxy routing merely because it exists in a shared list.

Lists belong to Ken, not an upstream auto-feed. Manual upstream mainland
refresh still uses tools/sync_china_direct.py; mainland overlap reviews must
now inspect both JPProxy.list and USProxy.list rather than search only inline
CN rows. No cron or client change. Protected General/DNS/TUN/nodes/MITM and
OS remain unchanged. Clients refresh configs AND referenced rule sets.

## Mainland DIRECT, owner exceptions, default proxy — 2026-11-06

Ken approved this design in SR Topic194 message1251. It supersedes
`CN_LIGHTWEIGHT_PROXY_V1` default DIRECT, not the rest of the profiles.
CN/CNR use marker `CN_CHINA_DIRECT_V1`; JP native manifest layout is
`china-direct-proxy-v1`.

Order: local/private destinations (and CNR owner-management DIRECT isolation),
existing explicit domain/keyword/IPv4 JP/US exceptions, one owner-hosted
`ChinaDirectDomains.list` DIRECT rule set, GEOIP CN DIRECT, default JP in
CN/Clash and US in CNR. Existing proxy overlaps intentionally win over the
mainland domain list. OS is not changed.

ChinaDirectDomains.list is the complete Loyalsoldier/clash-rules direct.txt
snapshot converted without broadening: upstream `+.domain` becomes
DOMAIN-SUFFIX, plain host becomes DOMAIN. Never strip subdomains from plain
upstream entries: that would incorrectly expand direct access. These are
mainland/direct-connectivity classifications, not legal nationality or a
complete definition of every foreign site. Retain existing explicit Google,
Apple push, OKX and other owner proxy exceptions ahead of the provider.
The overlap report is ChinaDirectDomains.overrides.json; snapshot revision,
source/output SHA256 and counts are ChinaDirectDomains.source.json.
GPL-3.0 attribution/license is kept in ChinaDirectDomains.LICENSE.

Maintenance is manual when Ken requests it. Run tools/sync_china_direct.py,
review both additions and removals plus exceptions, update the overlap report,
and commit/revalidate all consumers. The script only writes repository files;
it never schedules, publishes or updates a remote service by itself. Do not
silently subscribe clients to changing upstream URLs: clients use Ken's own
GitHub list. Do not accumulate upstream files into CN/CNR inline rule tables.

Clash emits a native classical/text HTTP provider pointed at the same owner
GitHub list, fetched using JP REA with the existing 86400s refresh interval.
It does not pass the huge list through the old JP filtered rule cache/inline
provider path. Preserve whole General/DNS/TUN/Host/node/MITM settings: no bulk
real-IP/TUN exclusions or application identity rules restored. CNR's five
previously omitted owner IP selectors are now explicit DIRECT so US default
does not unintentionally capture them. All existing explicit CN/CNR proxy
rows remain, in their old relative order; no unrelated business reassignment.

Source publication, native parser/provider acceptance, client refresh and
actual phone use are separate. No promises about gaming speed or browser
verification follow from rule counts. Refresh selected CN/CNR configs and the
new rule set; refresh Clash subscription/provider and confirm rule mode.
Rollback is a new GitHub revert of this change plus the matching JP code and
manifest transaction backup, not a force-push or whole old-profile restore.

## Lightweight explicit proxy rules, default DIRECT — 2026-11-05

Owner explicitly replaces the earlier rule-set/real-IP/TUN-exclusion layout
with `CN_LIGHTWEIGHT_PROXY_V1`. CN now contains 280 explicit domain/IPv4
proxy selectors plus `GEOIP,CN,DIRECT` and `FINAL,DIRECT` (282 rules). CNR
contains the same policy mapped to US, with the five retained owner-address
selectors omitted under its existing infrastructure isolation (277 rules).
The sixth excluded owner range was not present in the retained proxy set.
No RULE-SET, DOMAIN-SET, IP-ASN, DIRECT process/domain/IP rule or REJECT rule
remains. CN/Clash retain existing JP versus US assignments; CNR uses US only.
All targets not explicitly listed, including foreign sites, now use DIRECT.
GEOIP still relies on the client's normal geographic database.

The owner separately confirmed removing all eight proxy USER-AGENT rows and
the TikTok PROCESS-NAME row to keep domain/IP rules only. Existing TikTok,
OneDrive, PayPal and WhatsApp domain/keyword selectors remain; arbitrary
app-only destinations no longer receive an app-identity proxy override.
No Duolingo, Roam, battleroyale or trustd domain mapping is guessed.
The existing native Clash JP targets capitaland.com and ascottchina.com are
made explicit in shared CN (US in CNR) before removing enhancement additions.

Remove the entire General always-real-ip and tun-excluded-routes fields.
Preserve all other General values, including DNS, IPv4, each profile's own
update URL and HTTP skip-proxy exceptions, plus native node groups and Host.
CN's existing protected MITM bytes stay unchanged; no MITM material is copied
to CNR. The canonical Clash translator follows only native supported syntax;
Windows and phone clients refresh manually. OS and shared legacy rule-list
files are not edited or deleted by this conversion.

Rules follow the owner's usage order: AI/development, trading, Google/YouTube,
communications, banks/services, remaining explicit domains, broad keywords,
then IPv4 and the DIRECT tail. Cross-policy overlap dependencies retain the
old host-only and IP-only first-match decisions; 5,786 constructed host cases
and 397 IPv4 boundary cases are checked (actual counts in the build report).
Do not remove an earlier suffix merely because a later keyword has the same
policy: tiktok.polymarket.com must retain its earlier US suffix decision.
The earlier Telegram CIDRs now move behind explicit domains as requested;
requests with both a hostname and a matching IP deliberately prefer their
explicit domain policy. Mixed host-plus-IP behavior is not claimed identical.
Removing the old DIRECT exceptions intentionally exposes empornium.me to
the retained JP porn keyword. This is an explicit-rule policy consequence,
not proof of a network, DNS or livestream performance improvement.

The reproducible builder, tests and validation live in Genesis
ops/cn_lightweight_profiles/. Publication, canonical Clash composition/native
loading and actual client refresh remain separate acceptance stages. This
entry supersedes earlier instructions to retain rule-set layout, real-IP,
TUN exclusion fields, app identification and an implicit proxy FINAL.

## Slow verification resource path: scoped JP exception — 2026-11-05

Mac CN runtime cache contains cloudflare.com in CNMainlandDirect and no
earlier challenge exception. The owner reports 20–30 second verification
waits on Mac/home Wi-Fi and iPhone. Three interleaved downloads of the same
public Turnstile api.js on the Mac took 2.296/1.417/9.217 seconds via current
SR routing, versus 0.461/0.427/0.424 seconds through a temporary SSH SOCKS
tunnel to the existing JP host. Both paths followed the same redirect and
returned HTTP 200 with 86,756 bytes. SSH is not the Reality transport and
these measurements do not establish full browser challenge completion time.

Add DOMAIN-SUFFIX,challenges.cloudflare.com and DOMAIN-SUFFIX,twilio.com
to the existing CNServiceJP list, which precedes CNMainlandDirect. This
overrides only the challenge subtree of the broad cloudflare.com DIRECT
entry and explicitly keeps Twilio on JP before later IP/GEOIP fallbacks.
CNR consumes the same provider with its existing US exit. Native Clash
consumes its filtered classical provider, preserving its existing TUN and
all native configuration/client switches. No new provider is necessary.

Do not remove the existing Cloudflare parent DIRECT policy, broaden to
Cloudflare address ranges, change real-IP/DNS/TUN, or alter GreenCloud's
recent exact-host DIRECT routes and the CN-only ICBC compatibility trial.
A shared verification endpoint cannot automatically follow every embedding
site's policy. GreenCloud remains DIRECT while the challenge subtree now
uses the proxy; actual browser acceptance for each site is still required.
Do not claim IP splitting alone proves the entire reported wait, or that
this change bypasses Cloudflare validation. No CAPTCHA/login is automated.

Refresh the selected CN/CNR rule sets, reconnect, reopen the affected page,
and measure the verification delay. Source/native provider acceptance does
not prove devices have refreshed. Rollback removes only these two rows and
the accompanying comment, then republishes/refilters this one provider.

## GreenCloud confirmed working; consolidate exact hosts into DIRECT rule set — 2026-11-05

Owner reports the site now works and no obvious challenge is needed, then
requests a concise rule-set layout. Move the two exact DOMAIN rows for
cp.green.cloud and chat.green.cloud from CN.conf into the existing
CNMainlandDirect.list beside greencloudvps.com. Keep both exact matches;
do not widen to green.cloud or claim all verification delay was diagnosed.
CN references this provider with DIRECT and no earlier domain selector
matches the two hosts, preserving the CN policy while removing inline rules.

The existing DIRECT provider is also consumed by CNR and native Clash,
so their provider refreshes inherit these two approved DIRECT entries;
CNR proxy identity, management-IP isolation and OS sources remain unchanged.
Clash serves compatible classical DOMAIN rows, but its existing 24-hour
source/client caches may delay uptake. Publication does not prove a cached
Clash provider or any phone has refreshed. No generator changes or service
restarts are required for this source consolidation.

General, DNS, real-IP/TUN/skip-proxy, IPv6, nodes, game/bank priorities and
protected MITM are unchanged. Earlier CN-only trial notes below are history;
this shared rule-set placement supersedes their scope for these two hosts.
Rollback only these two provider rows plus the reviewed inline relocation,
never restore entire old profiles or unrelated rule-set contents.

## GreenCloud CN-only exact-host DIRECT trial — 2026-11-05

Owner approved aligning the observed cp.green.cloud and chat.green.cloud
hosts with greencloudvps.com's existing DIRECT policy. Add only these two
exact DOMAIN rules in CN before service sets; do not widen to green.cloud
or Cloudflare shared parents. PacketTunnel showed the two hosts using JP
FINAL while the main site and challenge apex used DIRECT. This change
makes these observed site routes consistent; it does not establish that
route mixing caused the challenge delay or that DIRECT will be faster.

Keep DNS/fallback, real-IP, skip-proxy, TUN, IPv6, nodes, game/bank rules,
protected MITM and shared challenge domains byte-for-byte unchanged.
CNR, OS and the JP canonical Clash generator/managed profile are outside
this CN-only phone trial and are not synchronized by this publication.
Do not infer that a changed CN hash has already been imported into Clash.

Refresh the CN configuration, reconnect and reopen the site for acceptance.
No actual browser challenge/login/transaction is performed by publishing.
If performance regresses, remove only these two exact DOMAIN rows and their
comment against then-current CN; do not restore an old entire configuration.

## ICBC enterprise iPhone HTTP-proxy compatibility trial — 2026-11-04

Owner reported the enterprise banking app displaying its own -1005 message,
"cannot resolve server address", with the iPhone CN profile enabled. No failing
hostname, phone DNS/connection log or off/on A/B result was provided yet.
Do not interpret this app code as a proven native iOS DNS error or claim a
confirmed root cause. Public AliDNS A queries for corporbank.icbc.com.cn,
corporwap.icbc.com.cn, corporbank-simp.icbc.com.cn, wap.icbc.com.cn and
m.icbc.com.cn returned answers during the investigation; that is not a test
of the phone's Wi-Fi/system DNS or proof of the app's actual endpoint.

CN already keeps icbc.com.cn and its wildcard in always-real-ip and routes
its .cn namespace DIRECT. Recent expanded real-IP/TUN exclusions did not add
an ICBC HTTP-proxy bypass. Add only icbc.com.cn and *.icbc.com.cn to CN's
native skip-proxy list, following the existing narrow CCB/ABC/PSBC pattern.
This is a scoped compatibility trial to avoid the system HTTP proxy entry,
not a guarantee to bypass TUN or cure every DNS failure. Do not broaden it
to all banks, change global resolvers/fallback/IPv6/TUN, remove real-IP, or
modify protected MITM. Existing regional/owner IP policies stay unchanged.
CNR, OS and native Clash are not changed for this iPhone-only report.

Refresh the CN configuration (not just the node subscription), reconnect
Shadowrocket, fully reopen the banking app and retry without transactions.
Phone acceptance remains pending; if still failing, obtain a short sanitized
DNS/connection excerpt with the failing hostname and a same-network SR off/on
comparison before further edits. Rollback removes only these two skip-proxy
entries against the then-current source; never restore an old entire profile.

## CN/CNR and native Clash IPv6 address cleanup - 2026-11-03

Owner requested removal of explicit IPv6 addresses because these clients use
IPv4. Remove 87 IPv6 entries from each SR tun-excluded-routes value; preserve
all 890 IPv4 entries in their original order. Remove eight IPv6 rules from
CNPushTelegramJP and 102 from CNIPDirect; derive the same 102 removals for
CNRIPDirect. All other rule rows, ordering and policy bindings remain unchanged.
CN and CNR keep ipv6=false and prefer-ipv6=false. Native canonical Clash must
also emit ipv6=false and dns.ipv6=false, closing the gap with Windows' existing
local IPv4 overrides; publish filtered providers without the 110 IPv6 rows.
Do not change Clash TUN or client switches. Leave OS and its separate providers
intact. Keep IPv4 rules, Bybit JP coverage, CNR US-only identity and management
IP exclusions. These are explicit address/rule removals, not modifications to
shared GeoIP/ASN binary databases. No latency or memory saving is measured.
Refresh both configurations and rule sets, then reconnect to load the changes.
Rollback only the reviewed IPv6 delta using source 1544ad7, preserving later edits.

## CN/CNR IPv6 disabled by owner request - 2026-11-03

Set General `ipv6 = false` in CN.conf and CNR.conf. Keep `prefer-ipv6 = false`.
This scoped change only disables the two Shadowrocket profiles' IPv6 support;
it does not change any domain/IP policy, DNS resolver, TUN exclusion, real-IP
pattern, node, or CNR US-only identity. Existing IPv6 rule/exclusion data is
retained. Clash and OS are outside this request; no client or server restart.
Refresh the selected CN/CNR configuration and reconnect Shadowrocket to load
the change. Source publication does not establish that the phone has refreshed,
nor prove a latency improvement. Rollback only the two `ipv6` values.

## Bybit iPhone API routing correction - 2026-11-03

Add bybit.biz, ng-dex.com and bybitx.global to CNServiceJP (108->111).
During the owner's controlled iPhone Bybit reproduction at 09:14:57-09:15:02,
api3.bybit.biz made 8 successful DIRECT connections and api3.ng-dex.com made
73. Both explicitly matched GEOIP,CN,DIRECT. The main www.bybit.com and the
previously added fingerprint SDK hosts already used JP, proving that the
earlier rule update was loaded but did not cover the app's API aliases.

Use parent suffixes to cover API/WS siblings before generic GeoIP routing.
bybit.biz and bybitx.global are also present in the official login allowlist.
ng-dex.com routing is justified by observed traffic during the controlled app
launch, not by an assertion of legal ownership. www.bybitx.global already
used FINAL JP; make that observed alias explicit to avoid future GeoIP drift.
Keep unrelated shared CDN/analytics parents unchanged. No IP keyword rules.

The two observed API destination addresses fall within the existing
43.168.0.0/14 TUN exclusion. Captured TCP flows nevertheless entered SR via
the local proxy or Fake-IP hostname mapping, then matched GEOIP DIRECT.
This patch fixes that observed decision; it does not guarantee interception
of future IP-only traffic that bypasses SR. Do not proxy the whole cloud
prefix or change game bypass routes without evidence of an IP-only leak.
General, DNS, Always Real IP, Skip Proxy, STUN and all TUN bytes stay unchanged.

CN and canonical native Clash use JP; CNR keeps its explicitly requested US
exit. Preserve node/monitoring identities, owner-IP exclusions and Windows
IPv4/TUN/core-isolation settings. Refresh the rule set and reconnect before
device acceptance; verify actual API connections use JP in a new phone log.
Source/candidate validation alone is not evidence of a successful login.
Raw phone logs remain private. See Genesis audits/20261103-bybit-phone-routing.
Rollback only these three added suffixes and their managed provider version.

## Bybit login dependency routing - 2026-11-03

Add three verified selectors to the existing CNServiceJP provider (105->108):
bybit-global.com, ffbbbdc6d3c353211fe2ba39c9f744cd.com, and the narrow SDK host
www.turingfraud.net. CN/canonical Clash use JP; CNR retains US under the
standing US-only instruction, pending any explicit owner change.

The official login page loads chunk16 d1a42468f8b43fc6dad9.js, SHA256
26fbefea43828164cf0a8b92291c2496eb48b6e1bd7940c569045dd00dec2d97.
Its login component invokes ByFingerPrintReport/getTxId. Production report
POST uses api.ffbbbdc6d3c353211fe2ba39c9f744cd.com; token initialization uses
https://www.turingfraud.net:30016. The SDK host's current resolved addresses
are AS132203, which the existing late IP-ASN rule sends DIRECT when a real
destination IP is available. Explicit domain coverage closes that conditional
fall-through without changing the whole ASN, TUN exclusions or STUN settings.
The alias with a hyphen is corroborated by an official announcement and auth
allowlist; it is distinct from the existing bybitglobal.com.

This is a verified coverage repair, not proof that the pictured iPhone request
used this Web SDK or that native login is fixed. A connection without hostname
information can still use the IP-based policy; phone capture and a fresh app
test remain necessary. Every app using www.turingfraud.net or its subdomains
shares this host exception; do not describe it as per-app routing. Do not widen
to turingfraud.net, shared CDN parents, whole cloud ASNs, or a guessed IP block.

Preserve all original entries/order, General/profile/node/DNS/TUN/real-IP and
domestic-game/bank/APNs/US boundaries. Current SDK sample destinations do not
overlap the977TUN exclusions. The address in the owner's screenshot is a
reported client egress IP, not a server destination to add or subtract.
Use native filtered Clash providers and preserve whole TUN/local switches and
the Windows-only IPv4/startup-isolation repair. Do not disable game STUN/voice.

Unauthenticated tests of https://api2.bybit.com/register/permission_v2 from
the Mac network path and JP VPS both returned JP/45.153.247.160 and no IP
restriction. They are neither iPhone path proof nor account eligibility.
Bybit restricts US/mainland-China API sources; CNR-US is not a usability
promise. Source and test evidence: Genesis audits/20261103-bybit-egress.
Rollback only these three selectors, preserving the preceding9UA cleanup.

## CN / CNR minimal equivalent cleanup - 2026-11-03

Remove only 9 USER-AGENT rows from CNCompatibility01 (7) and
CNCompatibility05 (2) that are covered by retained same-DIRECT wildcard
patterns. Both profiles already reference these shared lists. Keep every
remaining rule in its original position; no new wildcard or broader policy
is introduced. CN expands from 4805 to 4796 rules and CNR from 4799 to 4790.
This is a 0.19 percent rule cleanup, not a measured speed improvement.
Retain Bilibili* and MicroMessenger%20Client: the installed Clash adapter
uses these aliases to emit Windows process rules; removing all SR-redundant
aliases would change native Clash payloads.

Keep the 977 exact TUN CIDRs, 210 real-IP domain families (420 apex/wildcard
patterns), 12 Skip Proxy entries, all DNS settings and profile bytes. Exact
CIDR collapse and domain-parent audit found no safe further reduction.
Preserve game DIRECT, explicit CN JP banks/APNs/Bybit, US business rules,
CNR US-only identity/monitoring and its six owner-management-IP exclusions.
Never widen cloud/IP ranges or delete required proxy exceptions to meet a
rule-count target. General lists and routing rules serve different purposes.

These USER-AGENT rows are SR-only. The canonical Clash provider filter must
produce identical native payload bytes before and after this cleanup; no
Clash TUN/local switch, DNS, node, group or rule synchronization is needed
for unsupported source rows. Retain Windows-only IPv4 repair and native
desktop/backup-core isolation. Do not feed raw SR compatibility lists to
Mihomo. Profile and rule-set refresh on the phone is distinct from source
publication; no new iPhone A/B latency or CPU measurement was performed.

Rollback restores only the 9 removed rows from d7899346, preserving any
later edits. Evidence and exact deleted rows:
Genesis projects/infrastructure/jp-vpn-new/audits/20261103-cn-cnr-lightweight.

## Explicit Bybit routing - 2026-11-02

Add 16 DOMAIN-SUFFIX rows to the existing CNServiceJP.list: ten verified
Bybit parent domains (web, app assets, API and regional services) and six
narrow, officially documented regional API/WebSocket subtrees. CN and
canonical Clash use JP REA; CNR retains its US group and monitoring identity.
CN/CNR already share this provider, so their profile bytes/order are unchanged.

Previously no explicit Bybit domain rule existed. Unmatched connections still
passed IP/ASN/GeoIP rules before FINAL JP; omission does not prove every
request went DIRECT or explain the supplied Passkey failure. The owner reports
success with global JP, but a current failed-session connection capture is
not available. This change makes the verified Bybit destinations explicit
before broad domestic/IP fallback and is not authenticated-login acceptance.

Sources: https://bybit-exchange.github.io/docs/v5/guide,
https://bybit-exchange.github.io/docs/v5/ws/connect,
https://www.bybit.com/en/login and its directly loaded public service scripts.
The login page references s1.bycsi.com/fh-static.bycsi.com; its service config
includes bybitglobal.com. Regional documentation is endpoint ownership evidence,
not a request to change the account region or assurance of access eligibility.

Preserve geetest.com and Apple/iCloud routing: shared authentication services
are not Bybit-exclusive, and this phone's Passkey dependency is unconfirmed.
Do not add guessed brand aliases, shared-cloud IP ranges or global CDN parents.
No changes to General, domestic game/bank priorities, private credentials,
CNR management-IP exclusions or the entire Clash TUN section/local switches.
Use the native filtered CNServiceJP provider in Clash; validate provider load
and rule selection independently of phone/login success. Refresh both the
profile and its rule-set/provider cache before the owner retries the app.

Rollback only these 16 added provider rows, preserving subsequent edits;
retain the prior canonical provider/managed-manifest backup in the audit.
Evidence: Genesis projects/infrastructure/jp-vpn-new/audits/20261102-bybit-routing.

## GCloud parent coverage and exclusion cleanup - 2026-11-02

Owner authorized broader game-service parent matching after the Nov01 game
capture showed three tconnd hosts still receiving fake IPv6 addresses.
Use gcloudsvcs.com and gcloudgbs.com as explicit early DIRECT and real-IP
families, replacing three narrow tenants. Core rules13->12; CN/CNR real-IP
families211->210, native SR apex/wildcard patterns422->420. Preserve both
apex and wildcard: they are not duplicate matching semantics.

This is a deliberate user routing preference, not a claim that all endpoints
under these parents are physically in mainland China. Independent resolver
answers vary; China-located answers already fit existing CN exclusions.
Never add foreign cloud ranges or broaden 43/8 or129/8 from these domain rules.
Retain system DNS for DIRECT and all existing JP-bank/APNs/US priorities.
Future proven foreign-service exceptions require a specific host policy review.

TUN exclusions979->977: remove the127.0.0.0/8 entry rejected by the phone,
and redundant239.255.255.250/32 already covered by224.0.0.0/4. Every public
address previously excluded remains covered. No new IP space is bypassed;
all116 explicit foreign IP rules remain disjoint from exclusions. Existing
APNs/domain and IP precedence overlaps are intentional, not duplicates.

Preserve Skip Proxy12, other General values, rule-set order, nodes, CN private
sections, and CNR US-only identity/monitoring/six owner-IP exclusions.
Native Clash synchronizes the two parent filters and core provider only;
its entire TUN section and local client switches stay unchanged.

The23:53:49 iOS interface notification caused an in-process network settings
rebuild; no evidence establishes a CN setting error. Do not invent a network
handover fix, disable IPv6, disable UDP relay, or enable Include All Networks
to claim success. This repair closes routing coverage, not measured ping.

Rollback: restore only the two General keys and core provider from8330a714,
preserving later unrelated changes. Audit and release receipts live under
Genesis projects/infrastructure/jp-vpn-new/audits/20261102-cn-gcloud-bypass.
The owner refreshes subscribed clients; source/native-core validation does
not prove phone loading, physical bypass of every packet, or zero jitter.

## Domestic app coverage completion - 2026-11-01

Owner-approved completion of the audited domestic service/app list. This
supersedes the prior118-family count, without removing its coverage. CN/CNR
now have 211 real-IP domain families (422 SR apex/wildcard patterns).
The existing DIRECT and explicit JP/US rules remain. Add only
16 previously missing DOMAIN-SUFFIX entries to CNMainlandDirect:
360scdn.com, elongstatic.com, fqnovelstatic.com, hik-cloud.com, hikiot.com, hikmall.com, hikvision.com, hikvisionmall.com, hongguoduanju.com, id6.me, jianying.com, meituxiuxiu.com, shenzhenair.com, springairlines.com, vlabstatic.com, xhslink.com.
The provider has 3710 rows; all original rows and their order are preserved.
Do not delete routing rules because General has a DNS or IP bypass exception.

Coverage includes the requested mainland portals/apps, airlines/travel,
carrier authentication, official short links, domestic Hikvision platforms,
and narrow documented resource tenants. Biliapi aliases were corroborated
with identical first-party API/download payloads and official redirects.
The domestic Hikvision category does not identify the actual installed App
or prove that all camera/P2P/media sessions use the documented website domains.
Keep international WPS/CapCut/Hik-Connect separate. Do not widen shared public
cloud parents (bcebos, aliyuncs, qcloud, myqcloud) from one tenant's evidence.

TUN exclusions are 979 entries: original14 special/local ranges plus
879 IPv4 and 86 IPv6 safe domestic subnets. All prior963 exclusions
remain covered. The16 additions cover50 historical DNS-address gaps;13 are
supported by Oct28-Nov01 observations and3 only by older September exports.
Every addition is inside the frozen CN dataset, with all explicit foreign-IP
exceptions subtracted. Three additions are carved subnets, not raw MMDB rows.
Protect17 Google exceptions/1293 addresses and every explicit JP/US IP rule.
This is partial country coverage (~95.49% IPv4 addresses), not a traffic ratio,
complete China IPv6 coverage, or proof of improved phone latency.

Skip Proxy remains12 entries. It changes the system HTTP proxy entrance,
not the DIRECT rule or TUN bypass by itself. DNS resolvers/fallback, groups,
private CN sections, game/push/JP-bank/US priorities remain unchanged. CNR
retains its own US-only account/monitor/update identity, no MITM, and six
owner-management IP exclusions via build_cnr.py. Native Clash receives the
supported domain-rule and real-IP-filter changes; its whole TUN section and
client-local switches are preserved. The owner refreshes clients manually.

Rollback only these two General keys and the16 added provider rows using
the a709a538 baseline, preserving unrelated later edits and private sections.
Audit: Genesis projects/infrastructure/jp-vpn-new/audits/20261101-cn-app-completion.
No phone loading, full native App session, game ping or SR-off-equivalence
acceptance is inferred from source/native-core/server tests.

## Domestic shopping, banking, video and games — 2026-11-01

The owner expanded the real-IP/TUN audit to Dianping, Meituan, Ele.me, Alipay,
Taobao, Didi, JD, mainland NetEase/Tencent games, domestic live/video platforms,
mainland personal/corporate banking and government services. CN/CNR now contain
118 reviewed real-IP domain families (236 native SR apex/wildcard patterns).
Every added family already matches DIRECT; routing providers/order/nodes and
upstream DNS remain unchanged. Known explicit JP/US domains are not broadened.
Treat observed SDK/background hosts as connections, not proof of app use.

Only dedicated service/asset domains and narrow shared-cloud tenant names are
eligible. Never add all aliyuncs.com, qcloud.com, myqcloud.com or cloud ASNs.
Keep HSBC Hong Kong/ZA and other explicit proxy policies separate from mainland
banking; boc.cn is the verified mainland Bank of China scope, not boc.com.
gov.cn covers that namespace, not every government-related app or third party.

The preceding compact country sources and exception-subtraction method remain
authoritative. TUN exclusions total 963: original14 + 865 mainland IPv4 +
84 IPv6 prefixes. Preserve every previously excluded country address and add
only exact safe country parents of newly observed public addresses, if missing.
All17 legacy Google proxy exceptions (1293 IPv4 addresses) remain protected.
This is still partial country coverage; dynamic/foreign CDN addresses outside
the selected ranges retain existing routing. No full-China or no-latency claim.

Skip Proxy stays at its reviewed12 entries. It bypasses the system HTTP proxy
entry, not by itself the TUN. HTTP apps can still enter SR's local proxy even
when real-IP DNS and destination exclusions exist. Adding Skip Proxy is a
separate path/compatibility decision, not an established UDP-game ping cure.
The owner has not supplied a new phone path/latency acceptance measurement.

CNR keeps US identity/monitoring/update URL/no MITM and the six management-IP
rule exclusions. Native Clash receives only its supported DNS filter changes;
keep its entire TUN and installed client-local switches unchanged. Preserve the
canonical filter in any future Windows enhancement, including empty lists.
Phone loading, game/app path and speed require manual refresh and device tests.
Rollback only changed General values/comments to5f97d39 and the preceding managed
Clash manifest, preserving later unrelated edits and the prior52-family trial.

## Compact domestic real-IP and TUN bypass trial — 2026-11-01

Supersedes the narrow /29 trial and earlier empty Always Real IP instruction.
Owner now requests real addresses for habitual domestic DIRECT services plus
compact domestic IP bypass, retaining all 17 legacy Google proxy IP exceptions.
CN/CNR use 52 reviewed domain families (104 native SR apex and wildcard entries)
for Tencent games/video, WeChat, NetEase, Douyin/Toutiao/Xigua and Youku assets.
Do not collapse tenant-specific gcloud names to a shared cloud parent.
General lists are not DOMAIN-SUFFIX rules or remote RULE-SET references.

TUN exclusions comprise the original 14 local/special entries, 857 exact-subset
mainland IPv4 ranges and 81 IPv6 ranges. Select IPv4 prefixes <= /16 and IPv6
prefixes <= /30, supplement with the exact country parents of observed habitual
app and historical game/QoS IPs. Never fill foreign or unknown holes to reduce
the count. The selected IPv4 addresses cover 95.42% of the safe frozen country
set; this is address coverage, not traffic coverage or complete mainland bypass.
Unselected domestic addresses retain normal DIRECT handling through SR.

IPv4 provenance: Hackl0us/GeoIP2-CN release
e169e29f2c3d88af5695b210b91ea7d97cf86dda, Country.mmdb SHA256
4c1a58204dfd5afcb67d42db16235c7ccab4c7024db83ce58cc0074cd4377efc.
IPv6 provenance: original GeoLite2 Country from Loyalsoldier/geoip release
33824131927ddbc19c540f2a301cc4ef4e123478, built 2026-10-28.
This product includes GeoLite2 data created by MaxMind, available from
https://www.maxmind.com. Geolocation is evidence, not a physical-location guarantee.
Sources: https://github.com/Hackl0us/GeoIP2-CN and
https://github.com/Loyalsoldier/geoip/tree/33824131927ddbc19c540f2a301cc4ef4e123478.

Subtract every current explicit foreign-proxy IP rule before selecting ranges;
the 17 overlapping historical Google rules protect 1,293 IPv4 addresses.
Keep explicit JP banking/APNs, US businesses, provider order and all other
General fields unchanged. Preserve protected CN sections and CNR's US-only
identity, monitoring, update URL, owner-IP exclusions and absence of MITM.

Real DNS answers and IP exclusion are separate steps; neither DNS DIRECT nor
skip-proxy alone proves that packets avoid the tunnel. HTTP proxy paths can
still enter SR. Future foreign-policy domains resolving inside an excluded range
can bypass those domain rules, so retain the explicit-IP conflict audit.
Never exclude the Fake-IP range 198.18.0.0/15.

Clash receives only native +.domain fake-ip-filter entries from this list.
The entire Clash TUN and installed client-local switches stay untouched.
The source enhancement must preserve the canonical filter, including empty lists.
No unattended updater is added. Refresh subscriptions/configurations manually;
phone route loading, actual game bypass and latency improvement require device
verification. No SR-off-equivalent latency guarantee is made.
Rollback only these two General keys/comments to the backed-up bb223807 version,
and restore the preceding managed Clash manifest; preserve unrelated later edits.

## Minimal-supernet Delta TUN-bypass trial — 2026-11-01

At the owner's request, CN and CNR replace the two observed /32 exclusions
with 58.217.180.240/29, covering .240–.247 (eight addresses, six unobserved).
This is the smallest single CIDR containing .242 and .246. It is an intentional
trial expansion, not equivalent deduplication or a verified game server pool.
APNIC registers the addresses to CHINANET-JS (China Telecom Jiangsu);
RIPE routing data reports 58.217.176.0/21 originated by AS134756, whose APNIC
name is ChinaNet-NANJING-JISHAN-IDC. ISP allocation is not game ownership.
Do not substitute that /21, the registered /12, or a /24 without new evidence.

PacketTunnel evidence shows each of .242 and .246 as a DIRECT UDP relay
lasting 16–19 minutes with megabytes in both directions during Delta sessions.
These are observed match candidates, not a permanent or complete game subnet.
Keep the original 14 exclusions and every other General/routing value unchanged.
Do not add the 650xx QoS probe fleet, broad Tencent ranges, extra real-IP rules,
or unsupported profile versions of phone-global logging/Tunnel settings.

This changes the local handling of all matching destination IP traffic,
not its prior DIRECT egress. Future matches can use different IPs; no matching
target means the test cannot validate or reject the local-TUN hypothesis.
All ports and protocols to the six additional addresses bypass SR too,
including future domain-based JP/US policies pointing into this subnet.
There are no overlaps with current explicit provider IP rules.
Verify actual bypass and phone game behavior before calling this a fix.
Rollback replaces the /29 with the earlier two /32s, retaining unrelated edits.
Native Clash TUN is a standing exception and remains untouched; no compatible
Clash policy/provider/node/DNS change is required by this SR-only trial.
CNR keeps its US-only identity/monitoring and owner-IP exclusions.

## Owner rollback: original skip-proxy plus tplogin only — 2026-10-31

Supersedes the local/router expansion below. Restore the exact previous
11-item CN/CNR skip-proxy order and append only tplogin.cn, giving 12 unique
entries. Remove the newly added *.lan, asusrouter.com, falogin.cn, miwifi.com,
and router.asus.com. Retain the original localhost and *.local.
Canonical Clash removes the same five native rules and retains one exact
DOMAIN,tplogin.cn,DIRECT, giving 51 main rules; all providers stay unchanged.
Preserve all other General, previously effective TUN exclusions, routing,
node/account/monitor identities, protected MITM and entire Clash TUN settings.
This is an owner-requested rollback after renewed game stutter, not proof that
*.lan caused the stutter. Phone game acceptance remains pending after refresh.
Windows client-local system proxy bypass remains separate and unchanged.

## Local/router skip-proxy alignment — 2026-10-31

CN and CNR use one deduplicated 17-entry skip-proxy list: private IPv4 CIDRs,
local names, router-management hosts, then existing business exceptions.
localhost and *.local were already present; add *.lan and the five exact
router hostnames as requested, without widening them to entire parent domains.
All other General values, TUN exclusions, rules, nodes and MITM are preserved.

Canonical Clash translates these to native DIRECT rules using the existing
manager; add the missing local lan suffix rule and five exact router-domain
rules, while retaining one localhost/local rule each. Do not write skip-proxy into Mihomo
YAML. Verge's separate Windows system_proxy_bypass is client-local, cannot be
set by the subscription, and remains unchanged under manual client management.
The entire Clash TUN and DNS real-IP filter remain unchanged.

## Standing CN to CNR synchronization — 2026-10-31

Owner requests future CN routing/general optimizations to also update CNR unless
an explicit later task scope excludes it. Derive from current published CN,
including General and ordered Rule Sets, with CNR's own update-url and existing
US-only node/group/monitor identity. Map both CN JP and US targets to CNR US;
CNR remains a Shadowrocket subscription, not a separate Clash profile. Never
copy CN's protected MITM CA or embedded credentials to CNR.

Exclude exactly the six owner infrastructure IP match keys declared in
ops/usp_guest_subscription/build_cnr.py. They currently occur inside CNIPJP,
CNIPUS and CNIPDirect, so filtering only CNR's main file is insufficient.
CNRIPJP and CNRIPDirect are dedicated filtered lists; the owner-only CNIPUS
reference is omitted. Reuse all other CN lists, preserve their order and do not
remove these IP rules from CN/Clash. Exclusion removes explicit matches, not
access permission or all broader routes containing those addresses.

General now matches CN except its CNR update-url: empty Always Real IP,
fallback off, system DIRECT DNS / Ali proxy DNS, IPv6 true / prefer false,
current skip-proxy/TUN exclusions, and no STUN response spoofing. Jump's cloud
and current TURN exception precede media UDP DIRECT in CNR as well, targeting
its existing US node; no claim of JP performance measurements for CNR US.
The complete Clash TUN settings and existing CN/Clash remain unchanged here.

## Jump Desktop routing audit — 2026-10-31

Jump cloud coordination and the currently verified TURN endpoint use JP after
same-destination tests from two China home computers. jumpdesktop.com moves from
CNMainlandDirect to CNServiceJP. The verified turn.jumpdesktop.com IPv4 address
172.105.221.210/32 is also in CNServiceJP before generic UDP-media DIRECT, so raw
UDP TURN packets do not take a different route from the domain. Recheck that
single endpoint if official TURN DNS changes; no cloud ASN or broad subnet bypass.
Remove blanket Jump Desktop/JumpConnect process DIRECT rules so they do not
silently override service routing. Domestic peer IPs still use existing China
DIRECT fallbacks; LAN/private paths are not sent to JP. Other app policies,
General, empty real-IP lists and Clash TUN are unchanged. CNR/OS are separate.

Tests measure coordination HTTPS and TURN/STUN RTT, not Fluid screen throughput.
The iPhone export DBs were empty. Host logs show a recent UDP relayed session
with both JP and native-cellular peer candidates, not a complete iPhone 5G A/B.
Windows Jump Connect is a system service with a native direct TCP connection;
with Clash TUN off, subscription rules cannot force unproxied service sockets
through Clash. No Jump host proxy, Windows client or firewall setting is changed.

## Owner update: remove STUN response spoofing — 2026-10-31

Remove `stun-response-ip` and `stun-response-ipv6` from CN General. No custom
STUN response address remains in this source. This supersedes the earlier
owner-supplied spoof-address values below. The phone Settings > UDP > Disable
STUN switch remains a separate local setting; turn it off manually for a normal
STUN comparison. Do not alter other UDP options or claim a game-lag cure.
Clash never imported these unsupported SR options. Synchronize its CN source
revision only after proving the complete native output remains unchanged.
Keep real-IP exceptions empty and the whole Clash TUN section unchanged.

## Owner update: all Real IP exceptions removed — 2026-10-31

CN explicitly keeps `always-real-ip =` empty, clearing all 212 previous entries.
Canonical Clash uses native `dns.fake-ip-filter: []`; the explicit complete-CN
replacement mode clears both template defaults and managed additions, 110 to 0.
The future Windows enhancement also clears the list and cannot append old entries.
This supersedes the earlier real-IP preservation notes below. Existing skip-proxy,
all routing/providers, other General flags, upstream DNS, Hosts, groups and MITM
remain unchanged. CNR/OS are separate. Preserve the entire Clash TUN section and
local switches; do not enable TUN or synchronize CN TUN routes.

# CN Rule Set routing policy — 2026-10-31

Owner instruction supersedes the standalone-only / Clash-pin trial. CN.conf
uses 28 main rules and 15 CN-only classical Rule Sets. All 4,000 reviewed
DOMAIN-SUFFIX conditions and 642 explicit IP rows remain covered. Expanded
conditions are 4,775, unchanged from the previous reviewed profile. Main-file count is not the total number of matching conditions and
is not a phone latency benchmark. CNR, OS and existing shared lists stay intact.

Order: existing remote processes; Apple push
domain exception; core domestic games DIRECT; APNs/official Telegram IPs JP;
other domestic games DIRECT; explicit US business/downloads; explicit JP banks,
apps and video; other domestic DIRECT parents; legacy app/keyword compatibility;
UDP media fallbacks; JP/US/DIRECT IP supplements; Tencent ASN, China GeoIP,
FINAL JP. Broad domestic IP/ASN fallback must not capture explicit JP/US apps.
ZA/HSBC remain explicit JP. US uses the single-member US REA/US-Reality group;
TUIC provisioning is retained. Do not broaden shared GCloud or CDN tenant roots.

Owner confirms intermittent Wi-Fi/5G stalls and yfamilys YouTubeAd.sgmodule.
That module already rejects Googlevideo UDP and YouTube API UDP. The initially
published UDP/443 workaround was therefore redundant for this phone and has
been withdrawn from CN and Clash after reading the actual module. Do not call
that rule a fix. The module also performs video URL redirects/body rewriting;
its current template lacks argument defaults, but the current upstream script
explicitly ignores unresolved arguments and uses defaults. That is not proof
of a fatal parse error. No actual phone cache/script log or module-off A/B was
available; the owner cannot test now. No module/MITM/certificate change.

General uses native host/glob lists, not DOMAIN-SUFFIX directives. Main DNS
223.5.5.5/223.6.6.6, system DNS for DIRECT, both fallback flags false and empty
fallback address list remain unchanged, as do groups, Hosts, MITM and routing.
Owner General update 2026-10-31: replace tun-excluded-routes with the supplied
14 special/local IPv4/IPv6 entries and skip-proxy with the supplied 11 entries;
ipv6=true, prefer-ipv6=false, always-reject-url-rewrite=false,
stun-response-ip=1.1.1.1 and stun-response-ipv6=::1. Existing icmp-auto-reply
and private-ip-answer remain true. Commented example options are not applied;
existing use-local-host-item-for-proxy=true stays unchanged. STUN spoofing can
affect game/call NAT traversal and is not a complete WebRTC leak guarantee.
skip-proxy is proxy/TUN compatibility, not a UDP TUN bypass; modern SR is not
TCP-only. No ephemeral public game-IP bypass or guessed MTU settings.

Permanent owner compatibility requirement: translate only settings and rules
supported natively by the installed target Clash/Mihomo version. Skip and report
unsupported settings; never paste SR keys or accept silent unknown-key parsing
as proof. The managed General allowlist currently maps only ipv6 to global and
DNS ipv6. Owner's persistent exception: leave the whole Clash TUN section and
client switches unchanged; do not synchronize CN TUN exclusions or enable TUN
unless the owner explicitly requests a TUN change later. Existing native
DIRECT translation of skip-proxy is routing intent, not OS HTTP-proxy bypass.
SR-only STUN/rewrite/private-IP/ICMP switches and prefer-ipv6 are not copied.
CN TUN route exclusions are not synchronized to Clash. Windows client global
IPv6/TUN controls can override subscription values; manual refresh is distinct
from local control changes and actual game/video acceptance.

Canonical Clash now follows this CN authority instead of appending the old
static routing template. Native Mihomo uses NETWORK in logical rules, retains
Windows process/eastmoney exceptions, and filters every owner Rule Set through
/sr-rules/. Supported SR USER-AGENT patterns map to native Windows processes;
unmapped UA/URL syntax is omitted. China GeoIP intent keeps Clash's existing
IPs_CN CIDR provider to avoid a new GeoIP database bootstrap dependency.
No raw SR syntax or MITM is copied into Clash. Native output now has 52 rules,
16 referenced providers and 16,414 verified payload rows. Keep the legacy
rendering branch for partial/recovery manifests; complete mode is explicit.

Source model checks: 87,377 contexts / 14,615 historical connections have no
unexpected policy changes; no intentional transport-policy change remains. 16,032 source/native domain contexts agree. Windows Mihomo 1.19.32
validates raw/composed/future-enhanced YAML, actually loads all 16 providers
with exact API counts and 0 parser errors/WARN, and cold-downloads ASN.mmdb.
The preceding rule restoration passed forty-four staged Python tests. Two physical Mac interfaces each pass
YouTube/thumbnail/video-CDN public HTTPS endpoint probes checks. These are not real iPhone video playback or Wi-Fi/5G handoff tests.

Refresh CN remote configuration AND its 15 Rule Sets, then reconnect. Refresh
canonical Clash subscription and providers manually; the agent does not reload
active clients. Confirm actual phone video behavior after Wi-Fi/5G switching when practical.
If still affected, test only the YouTube ad module separately; this update
does not remove a locally installed module. Delta Force lag in SR global DIRECT
also remains a distinct unlocalized issue, not a routing-count success claim.

Source/runtime/rollback receipts: Genesis
projects/infrastructure/jp-vpn-new/audits/20261031-cn-rulesets-youtube.
Rollback uses a new SR revert to 13f9857 and the joint JP code/manifest/cache
backup. Never force-push or run the old standalone builder over this layout.
