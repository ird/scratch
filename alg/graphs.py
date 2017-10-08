""" graphs.py
Common graph algorithms using a dictionary implementation of graphs
"""


def enum_edges(G):
    res = []
    for n in G.keys():
        for x in G[n]:
            res.append((n, x))
    return res


def main():
    G = {
        'a': ['b', 'c', 'd'],
        'b': ['a', 'c', 'd', 'e'],
        'c': ['a', 'b', 'd', 'f'],
        'd': ['a', 'd', 'e', 'f'],
        'e': ['b', 'd', 'e'],
        'g': []
        }
    print(enum_edges(G))
    return


if __name__ == "__main__":
    main()
