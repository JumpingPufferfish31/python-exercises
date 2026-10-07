from utils.typing import Sortable


def sort_nested(nested_list: list[list[Sortable]]) -> list[list[Sortable]]:
    inner = []
    for sub_list in nested_list:
        inner.append(sorted(sub_list))
    return sorted(inner)
