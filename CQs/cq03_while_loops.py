"""Practice working with while loops."""

__author__ = "730487717"


def num_instances(phrase: str, search_char: str) -> int:
    """Counts how many times the character appears in the phrase."""
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
        index += 1
    return count
