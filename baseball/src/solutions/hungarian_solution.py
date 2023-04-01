import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite

# builds the corresponding complete weighted bipartite graph


def build_graph(n, m, a, s):
    B = nx.complete_bipartite_graph(n, m)
    left, right = nx.bipartite.sets(B)

    for _, (u, v) in enumerate(B.edges()):
        B[u][v]['weight'] = a[u] + s[u][v - n]

    print(left)
    print(right)

    print(B.edges(data=True))

    pos = dict()
    pos.update((n, (1, i)) for i, n in enumerate(left))
    pos.update((n, (2, i)) for i, n in enumerate(right))
    nx.draw(B, pos=pos)

    # plt.show()

    return B


def build_directed_equality_subgraph():
    pass


def initial_greedy_bipartite_matching(G):
    pass


def exists_M_augmentating_path():
    pass


def hungarian_solution(n, m, a, s):
    B = build_graph(n, m, a, s)
    pass


build_graph(5, 5, [0, 0, 0, 0, 0], [[0, 1, 3, 5, 7], [0, 0, 89, 0, 0], [
            2, 0, 21, 0, 0], [0, 0, 0, 23, 0], [0, 5, 0, 0, 0]])
