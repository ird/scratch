""" npuzzle.py
N-Puzzle solver """


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


def main():
    grid = [2, 1, 7, 4, 3, 6, 5, 0, 8]
    print(display(grid, 3))
    pass


if __name__ == "__main__":
    main()
