"""Practice with writing a function to find and remove max from list."""

__author__ = "730487717"


def find_and_remove_max(input: list[int]) -> int:
    """Returns the max int and removes all instances of max from list."""
    if len(input) == 0:
        return -1
    index: int = 1
    highest_num: int = input[0]
    while index < len(input):
        if input[index] > highest_num:
            highest_num = input[index]
        index += 1
    index = 0
    while index < len(input):
        if input[index] == highest_num:
            input.pop(index)
        else:
            index += 1
    return highest_num
