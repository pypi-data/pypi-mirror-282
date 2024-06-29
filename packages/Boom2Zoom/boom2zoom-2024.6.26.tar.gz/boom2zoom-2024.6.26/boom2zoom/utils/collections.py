from collections.abc import Sequence, Mapping
from typing import TypeVar

# TODO: Use Type Parameter Syntax when Nuitka supports it
K = TypeVar("K")
V = TypeVar("V")
T = TypeVar("T")


def reverse_map(input_map: Mapping[K, V]) -> dict[V, list[K]]:
    """Creates a reverse mapping of the input, where each value becomes a key mapped to a list of original keys.

    This function takes a mapping (e.g., a dictionary) and creates a new dictionary where:
    - Each value from the input becomes a key in the output.
    - Each key in the output is mapped to a list of all keys from the input that had the corresponding value.

    Args:
        input_map: The input mapping to reverse. Can be any mapping type (e.g., dict, defaultdict).

    Returns:
        A dictionary where each key is a value from the input mapping, and each value is a list of keys from the input
        that had that value.

    Example:
        >>> input_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
        >>> reverse_map(input_dict)
        {1: ['a', 'c'], 2: ['b'], 3: ['d']}
    """
    reversed_map: dict[V, list[K]] = {}
    for key, value in input_map.items():
        if value in reversed_map:
            reversed_map[value].append(key)
        else:
            reversed_map[value] = [key]
    return reversed_map


def slice_by_indices[T](seq: Sequence[T], index1: int, index2: int) -> list[T]:
    """Slices a sequence from index1 up to, and including, index2.

    Notes:
        - If index2 is less than index1, then items will be returned in reverse.
        - If the indices are equal, the list will have one item, the item at the index.

    Raises:
        IndexError: If either index is out-of-bounds.
    """

    if index1 < 0 or index1 >= len(seq):
        raise IndexError(f"Index1 out of bounds: {index1}")

    if index2 < 0 or index2 >= len(seq):
        raise IndexError(f"Index2 out of bounds: {index2}")

    if index1 == index2:
        return [seq[index1]]
    elif index1 < index2:
        return [seq[i] for i in range(index1, index2 + 1)]
    else:
        return [seq[i] for i in range(index1, index2 - 1, -1)]
