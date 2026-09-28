# SR

CN routes Ascott's verified first-party `discoverasr.com` and
`the-ascott.com` hostnames through the existing `rules/JPServices.list` and
`🇯🇵 JP REA`, ahead of mainland-IP routing. Each hostname has one rule owner.
Their shared CDN/cloud IPs are not fixed rules: one IP may serve unrelated
sites and may change without notice. The generated Clash subscription should
inherit the same domain rules; the OS profile is managed separately.
