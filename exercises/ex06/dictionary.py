"""Practice with writing dictionary utility functions."""

__author__ = "730487717"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Returns a dictionary with inverted keys & values of the input dictionary."""
    invert_dict: dict[str, str] = {}
    for key in input_dict:
        # remember for...in loop runs through keys not values for dicts
        if input_dict[key] in invert_dict:
            # check that value of input_dict is not key in invert_dict
            raise KeyError(
                "Error: duplicate values in input dictionary cannot become keys!"
            )
        else:
            invert_dict[input_dict[key]] = key
    return invert_dict


def favorite_color(color_dict: dict[str, str]) -> str:
    """Returns the most popular favorite color in a dictionary."""
    count_dict: dict[str, int] = {}
    max: int = 0
    fav_color: str = (
        ""  # create empty string to use later when returning favorite color
    )
    for color_key in color_dict:
        if color_dict[color_key] in count_dict:
            count_dict[color_dict[color_key]] += 1
        else:
            count_dict[color_dict[color_key]] = 1  # creates new key for each color
    for count_key in count_dict:
        if count_dict[count_key] > max:  # if greater than max, replace as new max
            max = count_dict[count_key]
            fav_color = count_key
    return fav_color


def count(input_list: list[str]) -> dict[str, int]:
    """Returns a dictionary counting how many times each value appeared in a list."""
    count_dict: dict[str, int] = {}
    # create empty dictionary that uses same pattern as favorite_color fn to be filled
    for value in input_list:
        if value in count_dict:
            count_dict[value] += 1
        else:
            count_dict[value] = 1
    return count_dict


def alphabetizer(input_list: list[str]) -> dict[str, list[str]]:
    """Returns a list of words in a dictionary organized by the first letter."""
    output_dict: dict[str, list[str]] = {}
    for element in input_list:
        lower_letter: str = element[0].lower()
        # create variable for first letter to make uniform capitalization
        if lower_letter in output_dict:
            output_dict[lower_letter].append(element)
            # originally +=element but was adding each letter individually
        else:
            element_list: list[str] = [element]
            # can create new list each time b/c adding new key to dict
            output_dict[lower_letter] = element_list
    return output_dict


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Updates a dictionary with the attendance for each day."""
    # use same method as alphabetizer fn to mutate dictionary
    if day in attendance:
        if student not in attendance[day]:
            # first submission problem: fn repeated names so add another if statement
            attendance[day].append(student)
    else:
        day_list: list[str] = [student]
        attendance[day] = day_list
