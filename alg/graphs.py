""" graphs.py
Common graph algorithms using a dictionary implementation of graphs
"""


def enum_edges(G):
    res = []
    for n in G.keys():
        for x in G[n]:
            res.append((n, x))
    return res


def is_path(G, start, dest):
    reachable = {}
    reachable[start] = ''
    for x in G[start]:
        reachable[x] = start
    open_set = list(reachable.keys())
    new_nodes = True
    while new_nodes:
        new_nodes = False
        to_search = []
        for x in open_set:
            for n in G[x]:
                if n not in reachable:
                    reachable[n] = x
                    new_nodes = True
                    to_search.append(n)
        open_set = to_search
    return dest in reachable


def main():
    G = {
        'a': ['b', 'c', 'd'],
        'b': ['a', 'c', 'd', 'e'],
        'c': ['a', 'b', 'd', 'f'],
        'd': ['a', 'd', 'e', 'f'],
        'e': ['b', 'd', 'e'],
        'f': ['c', 'd', 'x'],
        'g': [],
        'x': ['f']
        }
    print(enum_edges(G))
    print(is_path(G, 'a', 'g'))
    print(is_path(G, 'a', 'f'))
    return


if __name__ == "__main__":
    main()
