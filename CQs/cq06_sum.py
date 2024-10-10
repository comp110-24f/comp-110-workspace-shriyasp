"""Summing the elements of a list using different loops."""

__author__ = "730487717"


def w_sum(vals: list[float]) -> float:
    """Returns the sum of a list using a while loop."""
    index: int = 0
    sum: float = 0.0
    while index < len(vals):
        sum += vals[index]
        index += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Returns the sum of a list using a for...in loop."""
    sum: float = 0.0
    for elem in vals:
        sum += elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Returns the sum of a list using a for...in range loop."""
    sum: float = 0.0
    for idx in range(0, len(vals)):
        sum += vals[idx]
    return sum
