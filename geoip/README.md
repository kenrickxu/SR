# Ken GeoIP2-CN snapshot

Owner-requested mirror of [Hackl0us/GeoIP2-CN](https://github.com/Hackl0us/GeoIP2-CN), release Country.mmdb. Bytes are copied unchanged, not merged with a global database. See Country.source.json for the exact source revision, SHA256, byte size and database build metadata; Country.LICENSE preserves the upstream GPL-3.0 license. Upstream credits JMVoid/ipip2mmdb, 17mon/china_ip_list and metowolf/iplist; GeoIP is a MaxMind trademark.

Download: https://raw.githubusercontent.com/kenrickxu/SR/main/geoip/Country.mmdb

This is an MMDB IP-country lookup database, NOT a Shadowrocket RULE-SET or a domain subscription. Use it only via the client's supported custom GeoIP database setting. It answers mainland-China membership and must not replace a full-country database when GEOIP US/HK/other country routes are required. Mainland domain rules are separate and remain useful for CDN/domain exceptions.

This publication only hosts the file. No CN/CNR/OS General, rule ordering, DNS, node, MITM, Clash generator/database setting or client-local setting is changed. Uploading a file does not make a client use it automatically.

Updates are manual when Ken requests maintenance: resolve release HEAD, fetch the pinned Country.mmdb, verify the Git blob SHA, parse with a maintained MaxMind reader and perform representative lookups, compare hashes/build dates, update this file and metadata together, then verify the public raw URL byte-for-byte. Retain source/license attribution and review upstream license changes. No new scheduler or direct upstream tracking is installed. A successful parser/sample check does not prove perfect real-world geolocation.
