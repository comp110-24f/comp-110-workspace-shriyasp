"""Calculates the number of items and the cost of hosting a tea party."""

__author__ = "730487717"


def main_planner(guests: int) -> None:
    """Displays the number of items needed and the cost of a tea party."""
    # Must convert all int values to str values for print fn to work
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: "
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )  # assign people var from tea_bags fn & treats fn the value of guests var
    )


def tea_bags(people: int) -> int:
    """Calculates the number of tea bags needed."""
    return people * 2


def treats(people: int) -> int:
    """Calculates the number of treats needed."""
    return int(tea_bags(people=people) * 1.5)


# instead of multiplying by 2 and 1.5, call tea_bags and multiply by 1.5
# assign people variable for tea_bags fn the value assigned for treats fn


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the cost of the tea party."""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
