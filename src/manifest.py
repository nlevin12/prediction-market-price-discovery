"""Small, portable manifest utilities used by the public demonstration.

The full research pipeline uses immutable input manifests so a later run can verify
that it is using exactly the intended source files.  This module keeps that idea in
a compact form without distributing the underlying vendor data.
"""

from __future__ import annotations

import hashlib
from pathlib import Path

import pandas as pd


def sha256_file(path: str | Path, chunk_size: int = 1_048_576) -> str:
    """Return the SHA-256 digest of one file without loading it all into memory."""
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        while chunk := handle.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()


def build_manifest(root: str | Path, pattern: str = "*") -> pd.DataFrame:
    """Create a deterministic file manifest below *root*.

    Paths are stored relative to *root*, so the manifest remains portable across
    machines.  Directories are omitted and output is sorted deterministically.
    """
    root_path = Path(root).resolve()
    rows: list[dict[str, object]] = []
    for path in sorted(root_path.rglob(pattern)):
        if path.is_file():
            rows.append(
                {
                    "relative_path": path.relative_to(root_path).as_posix(),
                    "bytes": path.stat().st_size,
                    "sha256": sha256_file(path),
                }
            )
    return pd.DataFrame(rows, columns=["relative_path", "bytes", "sha256"])


def validate_manifest(root: str | Path, expected: pd.DataFrame) -> pd.DataFrame:
    """Compare a current directory manifest with an expected one.

    Returns one row per expected/current path, with a status of ``match``,
    ``missing``, or ``unexpected_or_changed``.
    """
    required = {"relative_path", "bytes", "sha256"}
    missing = required.difference(expected.columns)
    if missing:
        raise ValueError(f"Expected manifest lacks columns: {sorted(missing)}")

    current = build_manifest(root)
    merged = expected.merge(
        current,
        how="outer",
        on="relative_path",
        suffixes=("_expected", "_current"),
        indicator=True,
    )
    both = merged["_merge"].eq("both")
    equal = both & merged["bytes_expected"].eq(merged["bytes_current"]) & merged[
        "sha256_expected"
    ].eq(merged["sha256_current"])
    merged["status"] = "unexpected_or_changed"
    merged.loc[merged["_merge"].eq("left_only"), "status"] = "missing"
    merged.loc[equal, "status"] = "match"
    return merged.sort_values("relative_path", kind="stable").reset_index(drop=True)
