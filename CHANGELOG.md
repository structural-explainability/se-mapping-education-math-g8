# Changelog

All notable changes to this project will be documented in this file.

The format is based on **[Keep a Changelog](https://keepachangelog.com/en/1.1.0/)**
and this project adheres to **[Semantic Versioning](https://semver.org/spec/v2.0.0.html)**.

## [Unreleased]

---

## [0.1.0] - 2026-04-26

### Added

- Initial repository scaffold with `src/`, `data/`, and `docs/` structure
- Context declarations for NAEP, CCSS, Finland, Norway, PISA, and Singapore
- NOR definitions for Grade 8 mathematics (linear equations, statistics, probability)
- Mapping files for NAEP Grade 8 mathematics:
  - linear equations
  - statistics and probability
- Validation module for mapping files (`validate`)
- Coverage matrix generation (`matrix`)
- CLI entry points (`python -m se_mapping_education_math_g8 validate|matrix`)
- Initial coverage matrix output for NAEP mappings

---

## Notes on versioning and releases

- We use **SemVer**:
  - **MAJOR** – breaking changes to artifact structure or validation semantics
  - **MINOR** – backward-compatible additions to schema or validation rules
  - **PATCH** – fixes, documentation, tooling
- Versions are driven by git tags. Tag `vX.Y.Z` to release.
- Docs are deployed per version tag and aliased to **latest**.
- Sample commands:

```shell
# as needed
git tag -d v0.1.0
git push origin :refs/tags/v0.1.0

# new tag / release
git tag v0.1.0 -m "0.1.0"
git push origin v0.1.0
```

[Unreleased]: https://github.com/structural-explainability/se-mapping-education-math-g8/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/structural-explainability/se-mapping-education-math-g8/releases/tag/v0.1.0
