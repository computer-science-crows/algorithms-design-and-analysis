import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite
from math import inf

# builds the corresponding complete weighted bipartite graph


def build_graph(n, m, a, s):
    G = nx.complete_bipartite_graph(n, m)
    left, right = nx.bipartite.sets(G)

    for _, (u, v) in enumerate(G.edges()):
        G[u][v]['weight'] = a[u] + s[u][v - n]

    print(left)
    print(right)

    print(G.edges(data=True))

    pos = dict()
    pos.update((n, (1, i)) for i, n in enumerate(left))
    pos.update((n, (2, i)) for i, n in enumerate(right))
    nx.draw(G, pos=pos)

    # plt.show()

    return G


def initial_greedy_bipartite_matching(G: nx.Graph):
    left, right = nx.bipartite.sets(G)

    M = nx.Graph()

    for node in left if len(left) <= len(right) else right:
        max_weight = -inf
        max_neighbour = 0
        for neighbour in G.neighbors(node):
            if neighbour not in M.nodes() and G[node][neighbour]['weight'] > max_weight:
                max_weight = G[node][neighbour]['weight']
                max_neighbour = neighbour

        M.add_node(node)
        M.add_node(max_neighbour)
        M.add_weighted_edges_from([(node, max_neighbour, max_weight)])

    print(M.nodes())
    print(M.edges(data=True))

    return M


def default_vertex_labeling(G):
    left, right = nx.bipartite.sets(G)

    for node in left if len(left) <= len(right) else right:
        max_weight = -inf
        max_neighbour = 0
        for neighbour in G.neighbors(node):
            if G[node][neighbour]['weight'] > max_weight:
                max_weight = G[node][neighbour]['weight']
                max_neighbour = neighbour
        G.nodes[node]['h'] = ()
    pass


def build_directed_equality_subgraph(G, M):
    left, right = nx.bipartite.sets(G)

    G_h = nx.Graph()
    G_h.add_nodes_from(left, bipartite=0)
    G_h.add_nodes_from(right, bipartite=1)


def exists_M_augmentating_path():
    pass


def hungarian_solution(n, m, a, s):
    B = build_graph(n, m, a, s)
    initial_greedy_bipartite_matching(B)
    pass


hungarian_solution(5, 5, [0, 0, 0, 0, 0], [[0, 1, 3, 5, 7], [0, 0, 89, 0, 0], [
    2, 0, 21, 0, 0], [0, 0, 0, 23, 0], [0, 5, 0, 0, 0]])
