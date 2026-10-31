# CN standalone routing policy — 2026-10-31

CN.conf is now the single-file runtime rule authority. It has no RULE-SET,
DOMAIN-SET or exact DOMAIN entries. Complete domain names use DOMAIN-SUFFIX;
shared CDN/cloud namespaces retain necessary business-level boundaries rather
than being widened to the whole provider. Do not strip the public suffix with
naive last-two-label parsing or broaden OKX's Cloudflare alias to
com.cdn.cloudflare.net/cloudflare.net. Public Suffix List parsing is a boundary
check, not proof that a provider tenant owns every sibling.

Current reviewed output: 4,775 rules, including 4,000 DOMAIN-SUFFIX entries and
642 IP rows; the previous expanded profile had 5,088 logical rows. Forty-three
legacy keyword safeguards and existing app/process/media-port compatibility
selectors are retained. They are patterns, not exact DOMAIN entries; deleting
them could lose unknown service variants or raw-IP app handling. This is not
an all-domain throughput or phone latency benchmark.

Order:
1. Existing remote-access process exceptions.
2. Necessary domain exceptions such as Apple push before Apple DIRECT.
3. Core national games and SDK parents DIRECT (Delta/Honor of Kings/Peacekeeper).
4. Apple APNs and official Telegram IP exceptions, before media-port fallbacks.
5. Explicit US and JP service parents; ZA/HSBC and other JP apps never rely on
   FINAL. Named service rules precede broad domestic IP/ASN/GeoIP fallbacks.
6. Remaining games and domestic/approved DIRECT parents.
7. Existing keyword/app compatibility and FaceTime media-port fallbacks.
8. Other explicit IP policies, specific prefixes before parent networks.
9. Existing Tencent ASN, GEOIP CN DIRECT, FINAL JP.

Parent policies retain CN's existing QQ/Tencent/TCDNOS and domestic game scope.
Tencent's community game list mixes domestic and global SDKs; do not import all
of it as new DIRECT coverage. Observed project-specific gcloudsvcs/gcloudgbs
business parents and CN SDK endpoints are covered without forcing additional
shared global roots DIRECT. The original 263 game entries and three explicitly
reviewed resource endpoints are covered. No ephemeral game IP /32 pins or new
public tun-excluded-routes are introduced; dynamic domestic IPs retain the
reviewed IP/ASN/GEOIP fallbacks.

General has host/glob address lists, not DOMAIN-SUFFIX directives. Use parent
and *.parent pairs where apex and subdomains both need real IP; preserve local
and complex native patterns. Existing main DNS stays223.5.5.5/223.6.6.6,
DIRECT uses system DNS, fallback master/system flags remainfalse and the
fallback address list empty. IPv6, hijack DNS, node references and protected
MITM/Hosts remain unchanged. skip-proxy retains local/private/router scope;
it chooses proxy versus TUN handling, not a UDP bypass around Shadowrocket.

Telegram official14prefixes are explicitJP before generic UDP-port DIRECT;
this avoids treating Telegram traffic as FaceTime purely by port. Apple push
keeps its domain and published APNs-specific IP priority. Google's observed
gstatic domestic-direct behavior is retained; do not blindly pin all its static
assets to JP. Existing US routing uses the single-member US REA/US-Reality
selection and TUIC provisioning remains untouched.

Scope is CN ONLY. CNR.conf, OS.conf and all shared *.list files are unchanged.
Canonical CN Clash remains pinned to SR41d90d1 by the owner's explicit request;
do not sync this SR-only format/order into Clash without a later request and
its normal native-provider verification. No server/client restart is needed.

Refresh the CN remote configuration, then reconnect. CN no longer consumes
external rule-set refreshes. Actual same-phone game ping, locked-screen push,
bank use and network-switch acceptance are separate from source/selector tests.
No claim that this profile has eliminated Wi-Fi ping spikes or is fastest on
all networks. Source/report proof and the one-time reviewed builder are under
Genesis projects/infrastructure/jp-vpn-new/audits/20261031-cn-standalone.
The archived builder is tied to the old source hashes; it is not an updater.
Future CN edits go directly to this standalone file, with backup/regression
checks; never overwrite later edits by blindly rebuilding old list snapshots.

2026-10-31 follow-up: the owner reports Delta Force is smooth with SR OFF, but
lags with both CN routing and SR global DIRECT. Treat this as evidence against
JP/US rule selection being the sole cause; investigate the common SR-enabled
DNS/PacketTunnel/direct-UDP path and phone-wide UDP options. It does not prove
which of those components fails. Old connection tags are not RTT/loss evidence.
Do not claim that rule deletion cures this symptom or publish guessed MTU,
STUN/ICMP values, game-server IP pins or broad Tencent TUN exclusions.

Four additional IP rows were removed without changing any address or policy:
three exact adjacent-prefix merges in the uninterrupted JP priority block and
one later IPv6 row already fully covered by that block. All 4,000 domain rows
are unchanged and have no same-policy parent redundancy. Do not delete the
remaining independent roots merely to reduce the displayed rule count.
Observed gcloudsvcs/gcloudgbs project parents retain their boundaries; the whole
roots are shared SDK namespaces, not proven mainland-only game endpoints.
General, groups, Hosts and MITM bytes stay identical. Equivalence checks and
the still-open phone diagnosis are in Genesis audits/20261031-cn-tun-followup.

Sources:
- https://publicsuffix.org/list/
- https://core.telegram.org/resources/cidr.txt
- https://support.apple.com/en-us/102266
- https://github.com/v2fly/domain-list-community/tree/1daade8c4bb957d21d1f5c09c2b050d699e8e96c/data
- https://bank.za.group/
- https://www.hsbc.com.hk/
