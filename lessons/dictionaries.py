"""Examples of dictionary syntax with Ice Cream Shop order tallies."""

# Dictionairy type is dict[key_type, value_type],
# Dictionary literals are curly brackets
# that surround with key: value pairs
ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

# len evaluates to number of key-value entries
print(len(ice_cream))

# Add key-value entires using subscription notation
ice_cream["mint"] = 10

# Access values by their key using subscription notation
mint_orders: int = ice_cream["mint"]
print(mint_orders)

# Re-assign values by their key using assignment operators
ice_cream["mint"] = ice_cream["mint"] + 1
ice_cream["mint"] += 1

# Remove items by key using the pop method
print(ice_cream.pop("strawberry"))

# Test if a key is in the dictionary:
print("strawberry" in ice_cream)
print("vanilla" in ice_cream)

# Loop through items using for-in loops
# total: int = 0
# The variable (e.g. flavor) iterates over
# each key one-by-one in the dictionary.
for flavor in ice_cream:
    tally: int = ice_cream[flavor]
    print(f"{flavor}: {tally}")


def find_eligible(names: list[str], ages: list[int]) -> dict[str, int]:
    """Find the names and ages of all people old enough to rent a car!"""
    if len(names) != len(ages):
        raise ValueError("Diff lengths.")
    eligible_ppl: dict[str, int] = {}
    for idx in range(0, len(names)):
        if ages[idx] >= 25:
            eligible_ppl[names[idx]] = ages[idx]
    return eligible_ppl


names = ["Allan", "Ken", "Barbie"]
ages = [23, 26, 25]
renters: dict[str, int] = find_eligible(names, ages)
print(renters)

if "Ken" in renters:
    renters.pop("Ken")

print(renters)
