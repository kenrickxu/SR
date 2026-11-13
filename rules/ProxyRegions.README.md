## JP supplement consolidation — Ken5715,2026-11-13 HKT

CurrentCN has6rules/4sets: CNMediaDirect→MYProxy→USProxy→JPProxy→GEOIP,CN,DIRECT→FINAL,DIRECT. The previously61-row CNForeignProxy supplement is now merged intoJPProxy (281→342), with alloldselectors/options preserved and domainrows beforeIProws. No newforeign coverage beyond the alreadyapproved61; MY/US remainearlier. CNForeignProxy URL retained as comment-onlydeprecatedstub, notloaded; do notrecreateseparateCNForeignProxy set or importit atmaintenance. JPServices19/otherownerinputs keptuntouched. Review/provenance inProxyServices.review.json owner_jp_supplement_5715; futuredaily sourceupdatesmustpreserve theselocalownerrows andcurrentJPdata, not old281literalcount. ExistingYfamilyquarantine/thirteenfeeds remain.

SharedJPprovider data changes for consumers onrefresh, includingnative/iPhone/CNRaccordingtoexistinggroupmapping; this isnot a runtimeapply orautomatic clientrefresh. Preserve strictold6/old7/newmerged6 sourcecompatibility and GeneralRealIP0/Skip12/TUN14,17media/PushJP,US/MY,nodes/DNS/MITM/IPv6 and defaultDIRECT. OriginalCNURL/GeoIPCNorder/rollbackarchives/03:00+03:35deliveryalerts stay. Older5678/5701separatesupplement/fiveproviderwording below is supersededonlyonthisgrouping.

# JP and US owner proxy lists

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

