"""Basic syntax of lists."""

my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor


print(my_numbers)

# Add an item to the list
my_numbers.append(1.5)

print(my_numbers)

# Create an already populated list
game_points: list[int] = [102, 86, 94]
print(game_points)

# Subscription notation/indexing
print(game_points[2])
last_game: int = game_points[2]
print(last_game)

# Modifying elements
game_points[1] = 72
print(game_points)

# Getting the length
print(len(game_points))
y: int = len(game_points)
print(y)

# Remove an elements
game_points.pop(1)
print(game_points)

# Write a function called display
# Input: list[int]
# Return Value: None
# Loop over the input and print every value
# Try calling it on game_points


def display(input: list[int]) -> None:
    index: int = 0
    while index < len(input):
        print(input[index])
        index += 1


display(game_points)
