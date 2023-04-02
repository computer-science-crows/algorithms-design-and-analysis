import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite
from math import inf


def build_graph(n, m, a, s):
    """
        builds the corresponding complete weighted bipartite graph
    """

    G = nx.complete_bipartite_graph(n, m)
    left, right = nx.bipartite.sets(G)

    for _, (u, v) in enumerate(G.edges()):
        G[u][v]['weight'] = a[u] + s[u][v - n]

    # print(left)
    # print(right)

    # print(G.edges(data=True))

    pos = dict()
    pos.update((n, (1, i)) for i, n in enumerate(left))
    pos.update((n, (2, i)) for i, n in enumerate(right))
    nx.draw(G, pos=pos)

    # plt.show()

    return G


def default_vertex_labeling(G: nx.Graph):
    """
        Initializes h values of G with the default vertex labeling
    """

    left, right = nx.bipartite.sets(G)

    for node in left if len(left) <= len(right) else right:
        max_weight = -inf
        # max_neighbour = 0
        for neighbour in G.neighbors(node):
            if G[node][neighbour]['weight'] > max_weight:
                max_weight = G[node][neighbour]['weight']
                # max_neighbour = neighbour
        G.nodes[node]['h'] = max_weight

    for node in right if len(right) <= len(right) else left:
        G.nodes[node]['h'] = 0


def build_equality_subgraph(G: nx.Graph):
    """
        builds the corresponding equality subgraph G_h
    """

    left, right = nx.bipartite.sets(G)

    G_h = nx.Graph()
    G_h.add_nodes_from(left, bipartite=0)
    G_h.add_nodes_from(right, bipartite=1)

    for edge in G.edges():
        l = edge[0]
        r = edge[1]
        w = G[l][r]['weight']
        if G.nodes[l]['h'] + G.nodes[r]['h'] == w:
            G_h.add_weighted_edges_from([(l, r, w)])

    print(G_h.nodes())
    print(G_h.edges())

    return G_h


def initial_greedy_bipartite_matching(G_h: nx.Graph):
    """
        gets the initial matching of G_h using greedy tecniche
    """

    left = []
    right = []
    for node in G_h:
        if G_h.nodes[node]['bipartite'] == 0:
            left.append(node)
        else:
            right.append(node)

    M = nx.Graph()

    for node in left if len(left) <= len(right) else right:
        max_weight = -inf
        max_neighbour = 0
        for neighbour in G_h.neighbors(node):
            if neighbour not in M.nodes() and G_h[node][neighbour]['weight'] > max_weight:
                max_weight = G_h[node][neighbour]['weight']
                max_neighbour = neighbour

        if max_weight > -inf:
            G_h.nodes[node]['matched'] = True
            G_h.nodes[max_neighbour]['matched'] = True
            G_h[node][max_neighbour]['matched'] = True

            M.add_node(node)
            M.add_node(max_neighbour)
            M.add_weighted_edges_from([(node, max_neighbour, max_weight)])

    print(M.nodes())
    print(M.edges(data=True))

    return M


def exists_M_augmentating_path():
    pass


def hungarian_solution(n, m, a, s):
    G = build_graph(n, m, a, s)
    default_vertex_labeling(G)
    G_h = build_equality_subgraph(G)
    M = initial_greedy_bipartite_matching(G_h)
    pass


hungarian_solution(5, 5, [0, 0, 0, 0, 0], [[0, 1, 3, 5, 7], [0, 0, 89, 0, 0], [
    2, 0, 21, 0, 0], [0, 0, 0, 23, 0], [0, 5, 0, 0, 0]])
