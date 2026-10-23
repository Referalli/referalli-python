from __future__ import annotations

from typing import Generic, List, Optional, TypedDict, TypeVar

T = TypeVar("T")


class Page(TypedDict, Generic[T]):
    """One page of a list: pass ``next_cursor`` as ``starting_after`` for the next."""

    object: str
    data: List[T]
    has_more: bool
    next_cursor: Optional[str]
