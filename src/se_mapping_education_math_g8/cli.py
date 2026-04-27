"""Command-line interface for SE mapping examples."""

import sys

from se_mapping_education.matrix import run_matrix
from se_mapping_education.sort import run_sort
from se_mapping_education.validate import run_validate

from se_mapping_education_math_g8.verify_regimes import main as run_verify_regimes


def main(argv: list[str] | None = None) -> int:
    """Entry point for CLI commands."""
    if argv is None:
        argv = sys.argv[1:]

    if not argv:
        print("Usage: python -m se_mapping_education_math_g8 <command>")
        print("Commands: validate, matrix, sort, verify-regimes")
        return 1

    command = argv[0]

    if command == "sort":
        return run_sort()

    if command == "validate":
        return run_validate()

    if command == "matrix":
        return run_matrix()

    if command == "verify-regimes":
        return run_verify_regimes(argv[1:])

    print(f"Unknown command: {command}")
    return 1
