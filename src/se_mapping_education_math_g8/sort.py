"""sort.py - Normalize ordering in TOML files."""

from pathlib import Path
import tomllib
from typing import Any, cast

import tomli_w

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"


def load_toml(path: Path) -> dict[str, Any]:
    """Load a TOML file."""
    with path.open("rb") as file:
        return tomllib.load(file)


def write_toml(path: Path, data: dict[str, Any]) -> None:
    """Write a TOML file."""
    with path.open("wb") as file:
        tomli_w.dump(data, file)


def sort_acu(data: dict[str, Any]) -> bool:
    """Sort [[acu]] blocks by id. Returns True if changed."""
    raw = data.get("acu")
    if not isinstance(raw, list):
        return False

    acus = cast(list[dict[str, object]], raw)
    sorted_acus = sorted(acus, key=lambda x: cast(str, x.get("id", "")))

    if acus != sorted_acus:
        data["acu"] = sorted_acus
        return True

    return False


def sort_file(path: Path) -> bool:
    """Sort a single TOML file."""
    try:
        data = load_toml(path)
    except Exception:
        return False

    changed = False

    if sort_acu(data):
        changed = True

    if changed:
        write_toml(path, data)

    return changed


def run_sort() -> int:
    """Run sorting across data directory."""
    changed_files: list[Path] = []

    for path in sorted(DATA_DIR.rglob("*.toml")):
        if sort_file(path):
            changed_files.append(path)

    for path in changed_files:
        print(f"UPDATED: {path}")

    print(f"{len(changed_files)} files updated.")
    return 0
