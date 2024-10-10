"""Practice with using loops to make commonly used list functions."""

__author__ = "730487717"


def all(input: list[int], num: int) -> bool:
    """Checks if all the elements in a list match a given number."""
    index: int = 0
    num_of_matches = 0
    if len(input) == 0:  # check that list is not empty
        return False
    while index < len(input):
        if num == input[index]:
            num_of_matches += 1
        index += 1
    return num_of_matches == len(input)


def max(input: list[int]) -> int:
    """Returns the highest number in a list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    index: int = 1  # don't need to check index 0 again so start at 1
    highest_num: int = input[0]  # assign to first number in list
    while index < len(input):
        if input[index] > highest_num:
            highest_num = input[index]  # similar to card example from first class
        index += 1
    return highest_num


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Checks if list_1 and list_2 are deeply equal."""
    index: int = 0  # originally had separate index vars for list 1 & 2 but unnecessary
    num_of_matches: int = 0
    if len(list_1) == len(list_2):  # cannot assume lengths of list are equal so check
        while index < len(list_1):
            if list_1[index] == list_2[index]:
                num_of_matches += 1
            index += 1
    return num_of_matches == len(list_1) and num_of_matches == len(list_2)


def extend(list_1: list[int], list_2: list[int]) -> None:
    """Appends the values in list_2 to the end of list_1."""
    index: int = 0
    # need to use list_2 in while loop since list_2 is being concatenated to list_1
    while index < len(list_2):
        list_1.append(list_2[index])
        index += 1
