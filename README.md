# se-mapping-education-math-g8

[![Docs Site](https://img.shields.io/badge/docs-site-blue?logo=github)](https://structural-explainability.github.io/se-mapping-education-math-g8/)
[![Repo](https://img.shields.io/badge/repo-GitHub-black?logo=github)](https://github.com/structural-explainability/se-mapping-education-math-g8)
[![Python 3.15+](https://img.shields.io/badge/python-3.15%2B-blue?logo=python)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](./LICENSE)

[![CI](https://github.com/structural-explainability/se-mapping-education-math-g8/actions/workflows/ci-python-zensical.yml/badge.svg?branch=main)](https://github.com/structural-explainability/se-mapping-education-math-g8/actions/workflows/ci-python-zensical.yml)
[![Docs](https://github.com/structural-explainability/se-mapping-education-math-g8/actions/workflows/deploy-zensical.yml/badge.svg?branch=main)](https://github.com/structural-explainability/se-mapping-education-math-g8/actions/workflows/deploy-zensical.yml)
[![Links](https://github.com/structural-explainability/se-mapping-education-math-g8/actions/workflows/links.yml/badge.svg?branch=main)](https://github.com/structural-explainability/se-mapping-education-math-g8/actions/workflows/links.yml)

# Structural Explainability Mapping: Education Math Grade 8

> Grade 8 mathematics pilot mappings for linear equations and statistics.

Mapping example repositories include minimal `ctx` declarations sufficient for
self-contained validation and traceability.
Full source registries, dashboards, analytics, and public
participation systems belong in downstream organizations.

This repository illustrates multiple alignment types:

- NAEP / CCSS are grade-aligned
- Finland / Norway are band-aligned
- PISA is age-aligned
- Singapore is track + year (mapped approximately to grade)

## Coverage Matrix

See [coverage matrix](docs/en/coverage-matrix.md)

This matrix is a draft structural coverage artifact.
It shows declared mapping relations between source systems (CTX)
and normalized targets (NOR).
It does not evaluate curriculum quality, instructional effectiveness, or student performance.

Observed characteristics:

- NAEP is broad/aggregated: mostly overlaps
- Singapore is explicit for mean/median and data display
- CCSS contributes compare/displays and systems
- Finland / Norway are band-based and mostly overlaps
- Linear inequality appears only through NAEP so far

## Owns

- Grade 8 mathematics pilot mappings
- NOR units for the pilot scope
- coverage matrix artifacts

## Includes

### NOR scope

- linear equations
- systems of linear equations
- statistics and probability

### Source contexts

- NAEP Grade 8 mathematics
- CCSS Grade 8 mathematics
- selected international systems (Finland, Norway, PISA, Singapore)

### Derived outputs

- coverage matrix
- validation reports
- mapping examples

## Does Not Include

- complete K-12 mathematics coverage
- full source registries
- dashboards or public interfaces
- student outcome analysis
- policy interpretation or recommendations

## Command Reference

<details>
<summary>Show command reference</summary>

### In a machine terminal

After you get a copy of this repo in your own GitHub account,
open a machine terminal in `Repos` or where you want the project:

```shell
# Replace username with YOUR GitHub username.
git clone https://github.com/username/se-mapping-education-math-g8

cd se-mapping-education-math-g8
code .
```

### In a VS Code terminal

```shell
uv self update
uv python pin 3.15
uv sync --extra dev --extra docs --upgrade

uvx pre-commit install

git add -A
uvx pre-commit run --all-files
# repeat if changes were made
git add -A
uvx pre-commit run --all-files

# run
uv run python -m se_mapping_education_math_g8 sort
uv run python -m se_mapping_education_math_g8 validate
uv run python -m se_mapping_education_math_g8 matrix

# do chores
npx markdownlint-cli "**/*.md" --fix
uv run python -m ruff format .
uv run python -m ruff check . --fix
uv run python -m pyright
uv run python -m pytest
uv run python -m zensical build

# save progress
git add -A
git add -A
git push -u origin main
```

</details>

## Citation

[CITATION.cff](./CITATION.cff)

## License

[LICENSE](./LICENSE)

## Manifest

[SE_MANIFEST.toml](./SE_MANIFEST.toml)
