#!/usr/bin/env python3
"""Verify the domestic Douyin / international TikTok policy split."""

from __future__ import annotations

from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
DOMESTIC = (
    "api.douyin.com",
    "live.douyinliving.com",
    "api.iesdouyin.com",
    "log.snssdk.com",
    "api.amemv.com",
    "mon.bytedapm.com",
    "mon.ibytedapm.com",
    "video.douyinvod.com",
)
INTERNATIONAL = (
    "www.tiktok.com",
    "api.tiktokv.com",
    "cdn.tiktokcdn.com",
    "api.isnssdk.com",
    "api.byteoversea.com",
    "api.ibytedtos.com",
)


def matches(kind: str, value: str, domain: str) -> bool:
    value = value.lower().rstrip(".")
    domain = domain.lower().rstrip(".")
    if kind == "DOMAIN":
        return domain == value
    if kind == "DOMAIN-SUFFIX":
        return domain == value or domain.endswith("." + value)
    if kind == "DOMAIN-KEYWORD":
        return value in domain
    return False


def provider_rules(name: str):
    path = ROOT / "rules" / name
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith(("#", ";", "//")):
            continue
        fields = [field.strip() for field in line.split(",")]
        if len(fields) >= 2:
            yield fields[0].upper(), fields[1]


def policy_for(profile: str, domain: str) -> str:
    in_rules = False
    for raw in (ROOT / profile).read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line == "[Rule]":
            in_rules = True
            continue
        if in_rules and line.startswith("["):
            break
        if not in_rules or not line or line.startswith("#"):
            continue
        fields = [field.strip() for field in line.split(",")]
        if len(fields) >= 2 and fields[0] == "FINAL":
            return fields[1]
        if len(fields) < 3:
            continue
        kind, value, policy = fields[:3]
        if kind == "RULE-SET" and "/kenrickxu/SR/main/rules/" in value:
            name = Path(urlsplit(value).path).name
            if any(matches(rule_kind, rule_value, domain) for rule_kind, rule_value in provider_rules(name)):
                return policy
        elif matches(kind, value, domain):
            return policy
    raise RuntimeError(f"no policy for {profile}: {domain}")


def main() -> int:
    failures: list[str] = []
    for profile, expected_domestic, expected_international in (
        ("CN.conf", "DIRECT", "🇯🇵 JP REA"),
        ("OS.conf", "DIRECT", "DIRECT"),
    ):
        for domain in DOMESTIC:
            actual = policy_for(profile, domain)
            if actual != expected_domestic:
                failures.append(
                    f"{profile} domestic {domain}: {actual} != {expected_domestic}"
                )
        for domain in INTERNATIONAL:
            actual = policy_for(profile, domain)
            if actual != expected_international:
                failures.append(
                    f"{profile} international {domain}: "
                    f"{actual} != {expected_international}"
                )
    if failures:
        for failure in failures:
            print("FAIL", failure)
        return 1
    print(
        "PASS CN domestic=8 DIRECT international=6 JP_REA; "
        "OS domestic=8 DIRECT international=6 DIRECT"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
