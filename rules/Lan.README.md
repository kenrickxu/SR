# Owner LAN mirror and maintenance

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

