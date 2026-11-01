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
