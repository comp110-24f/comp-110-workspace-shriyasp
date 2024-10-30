"""Practice with unit tests for list utils."""

__author__ = "730487717"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens() -> None:
    """Tests that only_evens returns a list of even integers."""
    list_1: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(list_1) == [2, 4, 6]


def test_only_evens_mutate() -> None:
    """Tests that only_evens does not mutate input list."""
    list_2: list[int] = [7, 8, 2, 9, 4, 3]
    only_evens(list_2)
    #  list_2 should contain exact same values after only_evens called
    assert list_2 == [7, 8, 2, 9, 4, 3]


def test_only_evens_edge_case() -> None:
    """Tests that only_evens returns an empty list for input list with no even ints."""
    list_3: list[int] = [63, 5, 41, 25, 19, 37, 7]
    # make sure that no error occurs if there are no even numbers in list
    assert only_evens(list_3) == []


def test_sub() -> None:
    """Tests that sub returns a subset of the input list."""
    list_1: list[int] = [1, 2, 3, 4, 5, 6]
    assert sub(list_1, 2, 5) == [3, 4, 5]


def test_sub_mutate() -> None:
    """Tests that sub does not mutate input list."""
    list_2: list[int] = [7, 8, 2, 9, 4, 3]
    sub(list_2, 5, 3)
    # check that list_2 remains exactly the same after function is called
    assert list_2 == [7, 8, 2, 9, 4, 3]


def test_sub_edge_case() -> None:
    """Tests that when start index > length of list, empty list is returned."""
    list_3: list[int] = [39, 82, 56, 28, 54]
    assert sub(list_3, 5, 7) == []


def test_add_at_index() -> None:
    """Tests that add_at_index returns None."""
    list_1: list[int] = [43, 56, 78, 94, 22]
    assert add_at_index(list_1, 35, 2) is None


def test_add_at_index_mutate() -> None:
    """Tests that add_at_index does mutate input list."""
    list_2: list[int] = [7, 8, 2, 9, 4, 3]
    add_at_index(list_2, 5, 3)
    assert list_2 == [7, 8, 2, 5, 9, 4, 3]


# imported pytest at top of code rather than here to keep structure same across tests
def test_add_at_index_edge_case() -> None:
    """Tests that add_at_index gives IndexError for index > than length of list."""
    list_3: list[int] = [91, 83, 29, 77, 65]
    # use pytest instead of == to check if IndexError given
    with pytest.raises(IndexError):
        add_at_index(list_3, 49, 7)
