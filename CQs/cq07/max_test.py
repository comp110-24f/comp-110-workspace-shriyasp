"""Tests the use of find_and_remove_max."""

__author__ = "730487717"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max() -> None:
    """Tests that find_and_remove_max returns the expected value."""
    list_1: list[int] = [7, 4, 6, 9, 5, 9, 8]
    assert find_and_remove_max(list_1) == 9


def test_find_and_remove_max_mutate() -> None:
    """Tests that find_and_remove_max mutates list in expected way."""
    list_2: list[int] = [6, 3, 2, 8, 4, 3, 8, 8]
    find_and_remove_max(list_2)
    assert list_2 == [6, 3, 2, 4, 3]


def test_find_and_remove_max_edge_case() -> None:
    """Tests that if all numbers are max in list, mutates to empty list."""
    list_3: list[int] = [5, 5, 5, 5, 5, 5]
    find_and_remove_max(list_3)
    assert list_3 == []
