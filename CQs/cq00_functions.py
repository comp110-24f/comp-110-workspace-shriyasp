__author__ = "730487717"


def mimic(message: str) -> str:
    """Repeats the input back to you."""
    return message


def main() -> None:
    """Prints the result of mimic."""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
