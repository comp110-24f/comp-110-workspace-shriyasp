def get_first(input: list[str]) -> str:
    """Returns first element of list."""
    if len(input) == 0:
        return ""
    return input[0]


def remove_first(input: list[str]) -> None:
    """Removes first element of list."""
    input.pop(0)


def get_and_remove_first(input: list[str]) -> str:
    """Returns and removes first element of list."""
    first: str = input[0]
    input.pop(0)
    return first
