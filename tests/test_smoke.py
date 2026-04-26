# tests/test_smoke.py
"""Smoke tests for se_mapping_education_math_g8."""

from se_mapping_education.constants import ALLOWED_METHODS, ALLOWED_RELATIONS

from se_mapping_education_math_g8.cli import main


def test_constants_present():
    assert "equivalent" in ALLOWED_RELATIONS
    assert "expert_review" in ALLOWED_METHODS


def test_cli_no_args_returns_error():
    assert main([]) == 1


def test_cli_unknown_command_returns_error():
    assert main(["unknown"]) == 1
