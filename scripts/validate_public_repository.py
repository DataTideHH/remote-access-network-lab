"""Validate selected public-safety invariants for the repository.

This is a lightweight guardrail. It does not replace manual review of diffs,
private configuration, screenshots, account data or infrastructure exports.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
POLICY_EXAMPLE = REPOSITORY_ROOT / "examples" / "tailnet-policy.example.hujson"

REQUIRED_PATHS = (
    REPOSITORY_ROOT / "README.md",
    REPOSITORY_ROOT / "docs" / "access-control-model.md",
    REPOSITORY_ROOT / "docs" / "connection-tests.md",
    REPOSITORY_ROOT / "docs" / "security-considerations.md",
    REPOSITORY_ROOT / "docs" / "validation-checklist.md",
    POLICY_EXAMPLE,
)

TEXT_SUFFIXES = {
    ".conf",
    ".hujson",
    ".md",
    ".py",
    ".txt",
    ".yaml",
    ".yml",
}

FORBIDDEN_LITERALS = {
    "".join(("BBQ-", "BM6HJ64")): "real institution-managed desktop hostname",
    "".join(("BBQEDU-", "PF3NRBA0")): "real institution-managed notebook hostname",
}

FORBIDDEN_PATTERNS = (
    (
        re.compile(r"\b100(?:\.\d{1,3}){3}\b"),
        "real-looking Tailscale IPv4 address",
    ),
    (
        re.compile(r"-----BEGIN (?:OPENSSH |RSA |EC )?PRIVATE KEY-----"),
        "private-key material",
    ),
    (
        re.compile(r"\bSHA256:[A-Za-z0-9+/]{20,}={0,2}\b"),
        "SSH fingerprint",
    ),
    (
        re.compile(r"\btskey-[A-Za-z0-9-]{12,}\b"),
        "Tailscale authentication key",
    ),
)


def iter_public_text_files() -> list[Path]:
    """Return public text files that should be checked."""
    files: list[Path] = []
    for path in REPOSITORY_ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.name == ".gitignore" or path.suffix.lower() in TEXT_SUFFIXES:
            files.append(path)
    return sorted(files)


def validate_required_paths(errors: list[str]) -> None:
    for path in REQUIRED_PATHS:
        if not path.is_file():
            relative = path.relative_to(REPOSITORY_ROOT)
            errors.append(f"Missing required public-safety artifact: {relative}")


def validate_text_files(errors: list[str]) -> None:
    for path in iter_public_text_files():
        relative = path.relative_to(REPOSITORY_ROOT)
        text = path.read_text(encoding="utf-8")

        for literal, description in FORBIDDEN_LITERALS.items():
            if literal in text:
                errors.append(f"{relative}: contains {description}")

        for pattern, description in FORBIDDEN_PATTERNS:
            if pattern.search(text):
                errors.append(f"{relative}: contains {description}")

        if path.suffix.lower() == ".conf":
            for line_number, line in enumerate(text.splitlines(), start=1):
                stripped = line.strip()
                if not stripped.startswith("PrivateKey") or "=" not in stripped:
                    continue
                value = stripped.split("=", maxsplit=1)[1].strip()
                if not (value.startswith("<") and value.endswith(">")):
                    errors.append(
                        f"{relative}:{line_number}: contains a non-placeholder PrivateKey value"
                    )


def validate_policy_example(errors: list[str]) -> None:
    if not POLICY_EXAMPLE.is_file():
        return

    try:
        policy = json.loads(POLICY_EXAMPLE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"Policy example is not valid JSON-compatible HUJSON: {exc}")
        return

    grants = policy.get("grants")
    if not isinstance(grants, list) or len(grants) != 1:
        errors.append("Policy example must contain exactly one narrow grant")
        return

    expected_grant = {
        "src": ["tag:managed-client"],
        "dst": ["tag:remote-target"],
        "ip": ["tcp:22"],
    }
    if grants[0] != expected_grant:
        errors.append(
            "Policy example must grant only managed-client -> remote-target on tcp:22"
        )

    serialized = json.dumps(policy, sort_keys=True)
    for value in ("autogroup:internet", "0.0.0.0/0", "::/0", "*:*"):
        if value in serialized:
            errors.append(
                "Policy example contains an over-broad destination or capability: "
                f"{value}"
            )


def main() -> int:
    errors: list[str] = []
    validate_required_paths(errors)
    validate_text_files(errors)
    validate_policy_example(errors)

    if errors:
        print("Public repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Public repository validation passed.")
    print(f"Checked text files: {len(iter_public_text_files())}")
    print("Policy scope: tag:managed-client -> tag:remote-target on tcp:22")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
