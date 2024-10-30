"""Practice with common list utils."""

__author__ = "730487717"


def only_evens(input: list[int]) -> list[int]:
    """Returns a list of the even integers in a list of integers."""
    index: int = 0
    even_input: list[int] = []
    while index < len(input):
        # use modulo operation to check if even
        if input[index] % 2 == 0:
            even_input.append(input[index])
        index += 1
    return even_input


def sub(input: list[int], start: int, end: int) -> list[int]:
    """Returns a subset of the input list."""
    if start < 0:
        start = 0
    if end > len(input) - 1:
        end = len(input)
    index: int = start
    # make new variable called index so start variable not changed in while loop
    sub_list: list[int] = []
    # start with empty list so easy to return [] for the cases below
    if len(input) == 0 or start >= len(input) or end <= 0:
        return sub_list
    while index < end:
        sub_list.append(input[index])
        index += 1
    return sub_list


def add_at_index(input: list[int], element: int, index: int) -> None:
    """Adds element at a given index into a list."""
    if index > len(input) or index < 0:
        raise IndexError("Index is out of bounds for the input list")
    # raise IndexError for index values greater than length of list
    repeat: int = len(input) - index
    # create repeat variable so while loop repeats until element @ correct idx
    input.append(element)
    while repeat != 0:
        input.append(input[index])
        input.pop(index)
        repeat -= 1
        # decrease repeat var so that while loop functions until it "runs out"
