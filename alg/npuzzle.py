""" npuzzle.py
N-Puzzle solver """
from enum import Enum


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


def display(grid, size):
    # TODO: assertion that grid is a square
    i = 1
    res = ""
    for x in grid:
        if x == 0:
            res += "   "
        else:
            res += "{:-2d}".format(x) + " "
        if i % size == 0:
            res += "\n"
        i += 1
    return res


def move(grid, size, dir):
    return {
        Direction.UP: move_up(grid, size),
        Direction.DOWN: move_down(grid, size),
        Direction.LEFT: move_left(grid, size),
        Direction.RIGHT: move_right(grid, size)
    }[dir]


def swap(grid, i, j):
    grid[i], grid[j] = grid[j], grid[i]


def move_up(grid, size):
    p = grid.index(0)
    if p < size:
        pass
        # TODO: raise OOBException
    else:
        swap(grid, p, p - size)


def move_down(grid, size):
    pass


def move_left(grid, size):
    pass


def move_right(grid, size):
    pass


def main():
    grid = [2, 1, 7, 4, 3, 6, 5, 0, 8]
    print(display(grid, 3))
    move_up(grid, 3)
    print(display(grid, 3))
    pass


if __name__ == "__main__":
    main()
