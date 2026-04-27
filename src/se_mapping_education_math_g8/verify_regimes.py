"""verify_regimes.py - Verify regime compatibility for se-mapping-education-math-g8.

Run with:

uv run python -m se_mapping_education_math_g8 verify-regimes

or

uv run python -m se_mapping_education_math_g8 verify-regimes \
  --cases cases/ \
  --report reports/stress_report.md

Scope:

verify-regimes
  checks regime behavior:
  case outcomes against se-regimes PRS / BRK / INH rules

validate
  checks mapping source truth:
  schema, values, relation types, referential integrity
"""

import argparse
from pathlib import Path

from se_regimes.engine import build_coverage
from se_regimes.engine import run as run_cases
from se_regimes.registry import Registry
from se_regimes.registry import load as load_registry
from se_regimes.report import write_report


def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser for verify-regimes."""
    parser = argparse.ArgumentParser(
        prog="se_mapping_education_math_g8 verify-regimes",
        description="Verify regime compatibility for se-mapping-education-math-g8.",
    )
    parser.add_argument(
        "--cases",
        default="cases/",
        help="Cases directory (default: cases/).",
    )
    parser.add_argument(
        "--report",
        default="reports/stress_report.md",
        help="Report output path (default: reports/stress_report.md).",
    )
    return parser


def run_verify_regimes(
    cases_path: str = "cases/",
    report_path: str = "reports/stress_report.md",
) -> int:
    """Evaluate mapping cases against the SE regime registry and write the report."""
    cases_dir = Path(cases_path)
    report_file = Path(report_path)

    registry: Registry = load_registry()
    reg_warnings: list[str] = registry.validate()

    if reg_warnings:
        print("Registry warnings:")
        for w in reg_warnings:
            print(f"  ! {w}")

    if not cases_dir.exists():
        print(f"Cases directory not found: {cases_dir}")
        return 1

    results = run_cases(cases_dir, registry)
    coverage = build_coverage(results, registry)

    passed = sum(1 for r in results if r.passed)
    failed = sum(1 for r in results if not r.passed)

    print(f"Results: {passed} passed, {failed} failed ({len(results)} total)")

    if failed:
        for r in results:
            if not r.passed:
                print(f"  FAIL {r.case.id}")
                for msg in r.failures:
                    print(f"       {msg}")

    write_report(report_file, results, coverage, registry, reg_warnings)
    print(f"Report written to {report_file}")

    return 1 if (failed or reg_warnings) else 0


def main(argv: list[str] | None = None) -> int:
    """Entry point for verify-regimes command."""
    parser = build_parser()
    args = parser.parse_args(argv)
    return run_verify_regimes(cases_path=args.cases, report_path=args.report)
