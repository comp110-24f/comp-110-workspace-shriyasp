def remove_chars(msg: str, char: str) -> str:
    """Return a copy of msg with all instances of char removed."""
    copy: str = ""  # Set up empty str to copy values over
    index: int = 0
    while index < len(msg):
        if msg[index] != char:
            copy += msg[index]
        index += 1
    return copy


print(remove_chars(msg="football", char="o"))

word: str = "yoyo"  # global variable

print(remove_chars(word, "y"))


def chars(msg: str) -> str:
    idx: int = 0
    copy: str = msg
    while idx <= len(msg):
        print(idx)
        idx += 1
    return copy


a: str = "Hey"
b: str = "Hi"
chars(msg=a)
