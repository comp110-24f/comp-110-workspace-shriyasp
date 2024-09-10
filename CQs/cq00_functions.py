"""Practice with writing functions."""

__author__ = "730487717"


def mimic(message: str) -> str:
    """Repeats the input back to you."""
    return message


def main() -> None:
    """Prints the result of mimic."""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()


def greet(name: str) -> str:
    print("I'm so happy to see you " + name + "!")
    print(
        "Hello "
        + name
        + ", your name starts with an "
        + str(name[0])
        + " and ends with an "
        + str(name[len(name) - 1])
    )


def main() -> None:
    print(greet(name="Molly"))


main()
