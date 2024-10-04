"""EX03 - A version of Wordle for the word 'codes'."""

__author__ = "73048717"


def input_guess(secret_word_len: int) -> str:
    """Asks user to guess a word of a certain length."""
    input_word: str = input(f"Enter a {secret_word_len} character word: ")
    while len(input_word) != secret_word_len:
        # while loop needs to be for incorrect, not correct input to not cause error
        input_word = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return input_word


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Checks if user's character is in the secret word."""
    assert len(char_guess) == 1
    index: int = 0
    # create num_of_matches so that bool value returned is accurate for entire string
    num_of_matches: int = 0
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            num_of_matches += 1
        index += 1
    # if num_of_matches is greater than 0, there was a match so return True
    return num_of_matches > 0


def emojified(guess: str, secret: str) -> str:
    """Gives feedback to user on guess using different colored emojis."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    guess_checker: str = ""
    while index < len(guess):
        # use if, elif, else for three possible scenarios
        if guess[index] == secret[index]:
            index += 1
            guess_checker += GREEN_BOX
        elif contains_char(secret_word=secret, char_guess=guess[index]):
            # need to call contains_char to check if char anywhere in word
            index += 1
            guess_checker += YELLOW_BOX
        else:
            index += 1
            guess_checker += WHITE_BOX
    return guess_checker


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    guess_word: str = ""  # empty string
    while turn <= 6 and guess_word != secret:
        # need to check num of turns and that guess is not correct or will keep going
        print(f"=== Turn {turn}/6 ===")
        guess_word = input_guess(len(secret))
        print(emojified(guess=guess_word, secret=secret))
        if guess_word == secret:
            print(f"You won in {turn}/6 turns!")
        else:
            turn += 1
    if turn > 6:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
