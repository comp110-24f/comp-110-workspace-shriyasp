"""Mutating functions."""

__author__ = "730487717"


def manual_append(input: list[int], num: int) -> None:
    """Adds num to the end of the input list."""
    input.append(num)


def double(input: list[int]) -> None:
    "Doubles every item in the input list."
    index: int = 0
    while index < len(input):
        input[index] = input[index] * 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)
print(list_2)
print(list_1)
