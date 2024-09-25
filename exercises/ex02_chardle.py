"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730487717"


def input_word() -> str:
    """Asks the user for a 5-character word."""
    five_character_word: str = input("Enter a 5-character word: ")
    if len(five_character_word) == 5:
        return five_character_word
    else:
        print("Error: Word must contain 5 characters.")
        # Exit should occur after error message prints.
        exit()


def input_letter() -> str:
    """Asks the user for a letter."""
    character: str = input("Enter a single character: ")
    if len(character) == 1:
        return character
    else:
        print("Error: Character must be a single character.")
        exit()


def contains_char(word: str, letter: str) -> None:
    "Searches for letter in word and returns how many times it appears."
    print("Searching for " + letter + " in " + word)
    num_of_matches: int = 0
    # Use if statement to check at each index from 0-4 for 5-character word.
    if word[0] == letter:
        print(letter + " found at index 0")
        num_of_matches = num_of_matches + 1
    if word[1] == letter:
        print(letter + " found at index 1")
        num_of_matches = num_of_matches + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        num_of_matches = num_of_matches + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        num_of_matches = num_of_matches + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        num_of_matches = num_of_matches + 1
    # Need if/else statements for 0, 1, and more than one instance.
    # Should check condition in increasing order so that more than 1 is covered by else.
    if num_of_matches == 0:
        print("No instances of " + letter + " found in " + word)
    elif num_of_matches == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(num_of_matches) + " instances of " + letter + " found in " + word)


def main() -> None:
    """Combines previously defined functions into one function."""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
