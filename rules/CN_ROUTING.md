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
