# CN Rule Set routing policy — 2026-10-31

Owner instruction supersedes the standalone-only / Clash-pin trial. CN.conf
uses 29 main rules and 15 CN-only classical Rule Sets. All 4,000 reviewed
DOMAIN-SUFFIX conditions and 642 explicit IP rows remain covered. Expanded
conditions are 4,776 (previous 4,775 plus one video transport compatibility
rule). Main-file count is not the total number of matching conditions and
is not a phone latency benchmark. CNR, OS and existing shared lists stay intact.

Order: existing remote processes; Googlevideo transport exception; Apple push
domain exception; core domestic games DIRECT; APNs/official Telegram IPs JP;
other domestic games DIRECT; explicit US business/downloads; explicit JP banks,
apps and video; other domestic DIRECT parents; legacy app/keyword compatibility;
UDP media fallbacks; JP/US/DIRECT IP supplements; Tencent ASN, China GeoIP,
FINAL JP. Broad domestic IP/ASN fallback must not capture explicit JP/US apps.
ZA/HSBC remain explicit JP. US uses the single-member US REA/US-Reality group;
TUIC provisioning is retained. Do not broaden shared GCloud or CDN tenant roots.

Wi-Fi/5G switching can leave a video session unusable even while the app feed
refreshes; the owner reports restarting SR restores video and a YouTube ad
module is enabled. Add only:
AND,((PROTOCOL,UDP),(DST-PORT,443),(DOMAIN-SUFFIX,googlevideo.com)),REJECT
This is a bounded compatibility mitigation that lets video retry TCP through
JP; it is not proof that QUIC was the root cause or phone handoff is cured.
Other UDP/443 traffic, national games and node TUIC transport are not globally
blocked. The local ad module is not present in CN.conf and remains a separate
possible cause. No protected MITM/certificate change or local module edit.

General uses native host/glob lists, not DOMAIN-SUFFIX directives. Main DNS
223.5.5.5/223.6.6.6, system DNS for DIRECT, both fallback flags false and empty
fallback address list remain unchanged, as do groups, Hosts, MITM and other
General bytes. skip-proxy is proxy/TUN compatibility, not a UDP TUN bypass.
No ephemeral game IP pins, broad public TUN exclusions or guessed MTU settings.

Canonical Clash now follows this CN authority instead of appending the old
static routing template. Native Mihomo uses NETWORK in logical rules, retains
Windows process/eastmoney exceptions, and filters every owner Rule Set through
/sr-rules/. Supported SR USER-AGENT patterns map to native Windows processes;
unmapped UA/URL syntax is omitted. China GeoIP intent keeps Clash's existing
IPs_CN CIDR provider to avoid a new GeoIP database bootstrap dependency.
No raw SR syntax or MITM is copied into Clash. Native output has 62 rules,
16 referenced providers and 16,414 verified payload rows. Keep the legacy
rendering branch for partial/recovery manifests; complete mode is explicit.

Source model checks: 87,377 contexts / 14,615 historical connections have no
unexpected policy changes; two synthetic video UDP/443 cases intentionally
reject. 16,032 source/native domain contexts agree. Windows Mihomo 1.19.32
validates raw/composed/future-enhanced YAML, actually loads all 16 providers
with exact API counts and 0 parser errors/WARN, and cold-downloads ASN.mmdb.
Forty-four staged Python tests pass. Two physical Mac interfaces each pass
YouTube/thumbnail/video-CDN public HTTPS endpoint probes and native video-UDP
rejection. These are not real iPhone video playback or Wi-Fi/5G handoff tests.

Refresh CN remote configuration AND its 15 Rule Sets, then reconnect. Refresh
canonical Clash subscription and providers manually; the agent does not reload
active clients. Confirm actual phone video behavior after Wi-Fi/5G switching.
If still affected, test only the YouTube ad module separately; this update
does not remove a locally installed module. Delta Force lag in SR global DIRECT
also remains a distinct unlocalized issue, not a routing-count success claim.

Source/runtime/rollback receipts: Genesis
projects/infrastructure/jp-vpn-new/audits/20261031-cn-rulesets-youtube.
Rollback uses a new SR revert to 13f9857 and the joint JP code/manifest/cache
backup. Never force-push or run the old standalone builder over this layout.
