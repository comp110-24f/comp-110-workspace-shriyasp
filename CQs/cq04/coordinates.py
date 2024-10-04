"""Practice with using nested while loops."""

__author__ = "730487717"


def get_coords(xs: str, ys: str) -> None:
    index_xs: int = 0
    index_ys: int = 0
    while index_xs < len(xs):
        while index_ys < len(ys):
            print("(" + xs[index_xs] + "," + ys[index_ys] + ")")
            index_ys += 1
        index_xs += 1
        index_ys = 0
