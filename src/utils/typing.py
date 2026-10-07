from typing import Optional, Protocol, TypeAlias, TypeVar


T = TypeVar('T')
Nullable: TypeAlias = Optional[T]

class SortableProtocol(Protocol):
    def __lt__(self: T, __other: T) -> bool: ...

Sortable = TypeVar('Sortable', bound=SortableProtocol)
