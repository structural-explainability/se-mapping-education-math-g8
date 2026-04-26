"""types.py - Shared types for SE mapping validation.

Keep types aligned with
se-mapspec/data/alignment/alignment-schema.toml.
"""

from typing import Literal, NotRequired, TypedDict

Method = Literal[
    "manual",
    "expert_review",
    "llm_assisted",
    "rule_based",
    "imported",
]

Relation = Literal["equivalent", "broader", "narrower", "overlaps", "none"]

ALLOWED_METHODS: frozenset[str] = frozenset(
    {
        "manual",
        "expert_review",
        "llm_assisted",
        "rule_based",
        "imported",
    }
)

ALLOWED_RELATIONS: frozenset[str] = frozenset(
    {
        "equivalent",
        "broader",
        "narrower",
        "overlaps",
        "none",
    }
)


class Alignment(TypedDict):
    """A single source-to-target mapping assertion."""

    source_id: str
    target_id: str
    relation: Relation
    confidence: float
    method: Method
    human_validated: bool
    source_text: NotRequired[str]
    note: NotRequired[str]


class Context(TypedDict):
    """Declared context for a mapping file."""

    id: str
    type: str
    name: NotRequired[str]


class MappingFile(TypedDict, total=False):
    """Parsed TOML structure for a mapping file."""

    ctx: Context
    alignment: list[Alignment]
