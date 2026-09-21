#!/usr/bin/env python3
"""Fail when owner rule lists contain identical normalized rules."""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
RULES = ROOT / "rules"
DOMAIN_RULES = {"DOMAIN", "DOMAIN-SUFFIX", "DOMAIN-KEYWORD"}


def normalize(raw: str) -> str | None:
    line = raw.strip()
    if not line or line.startswith(("#", ";", "//")):
        return None
    fields = [item.strip() for item in line.split(",")]
    kind = fields[0].upper()
    if len(fields) > 1 and kind in DOMAIN_RULES:
        fields[1] = fields[1].lower().rstrip(".")
    fields[0] = kind
    return ",".join(fields)


def cn_domain_set_overlaps() -> list[str]:
    """Find later CN DOMAIN-SET entries shadowed by any earlier domain rule."""
    config = (ROOT / "CN.conf").read_text(encoding="utf-8")
    in_rules = False
    selectors: list[tuple[str, str, str, str]] = []
    overlaps: list[str] = []

    for raw in config.splitlines():
        line = raw.strip()
        if line == "[Rule]":
            in_rules = True
            continue
        if in_rules and line.startswith("["):
            break
        if not in_rules or not line or line.startswith("#"):
            continue
        fields = [item.strip() for item in line.split(",")]
        if len(fields) < 3:
            continue
        kind, value, policy = fields[:3]
        if kind == "RULE-SET" and "/kenrickxu/SR/main/rules/" in value:
            name = Path(urlsplit(value).path).name
            path = RULES / name
            for number, provider_raw in enumerate(
                path.read_text(encoding="utf-8").splitlines(), 1
            ):
                provider = normalize(provider_raw)
                if provider is None:
                    continue
                provider_fields = provider.split(",")
                if provider_fields[0] in DOMAIN_RULES:
                    selectors.append(
                        (
                            provider_fields[0],
                            provider_fields[1],
                            policy,
                            f"{name}:{number}",
                        )
                    )
        elif kind == "DOMAIN-SET" and "/kenrickxu/SR/main/rules/" in value:
            name = Path(urlsplit(value).path).name
            path = RULES / name
            for number, domain_raw in enumerate(
                path.read_text(encoding="utf-8").splitlines(), 1
            ):
                domain = domain_raw.strip().removeprefix("+.").removeprefix(".").lower()
                if not domain or domain.startswith(("#", ";")):
                    continue
                owner = next(
                    (
                        f"{location} ({selector_policy})"
                        for selector_kind, selector, selector_policy, location in selectors
                        if (
                            selector_kind == "DOMAIN"
                            and domain == selector
                        )
                        or (
                            selector_kind == "DOMAIN-SUFFIX"
                            and (
                                domain == selector
                                or domain.endswith("." + selector)
                            )
                        )
                        or (
                            selector_kind == "DOMAIN-KEYWORD"
                            and selector in domain
                        )
                    ),
                    None,
                )
                if owner is not None:
                    overlaps.append(
                        f"{name}:{number} {domain} ({policy}) <= {owner}"
                    )
            break
        elif kind in DOMAIN_RULES:
            selectors.append((kind, value.lower().rstrip("."), policy, "CN.conf"))
    return overlaps


def main() -> int:
    occurrences: dict[str, list[str]] = defaultdict(list)
    effective = 0
    for path in sorted(RULES.glob("*.list")):
        for number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            rule = normalize(raw)
            if rule is None:
                continue
            effective += 1
            occurrences[rule].append(f"{path.name}:{number}")

    duplicates = {
        rule: locations
        for rule, locations in occurrences.items()
        if len({item.split(":", 1)[0] for item in locations}) > 1
    }
    if duplicates:
        for rule, locations in sorted(duplicates.items()):
            print(f"DUPLICATE {rule} => {'; '.join(locations)}")
        print(
            f"FAIL lists={len(list(RULES.glob('*.list')))} "
            f"rules={effective} duplicates={len(duplicates)}"
        )
        return 1

    domain_set_overlaps = cn_domain_set_overlaps()
    if domain_set_overlaps:
        for overlap in domain_set_overlaps:
            print(f"DUPLICATE CN_DOMAIN_SET {overlap}")
        print(f"FAIL cn_domain_set_overlaps={len(domain_set_overlaps)}")
        return 1

    print(
        f"PASS lists={len(list(RULES.glob('*.list')))} "
        f"rules={effective} exact_cross_file_duplicates=0 "
        "cn_domain_set_overlaps=0"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
