import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite
from math import inf


def default_vertex_labeling(G: nx.Graph):
    """
        Initializes h values of G with the default vertex labeling
    """

    left, right = nx.bipartite.sets(G)

    for node in left:
        max_weight = -inf
        # max_neighbour = 0
        for neighbour in G.neighbors(node):
            if G[node][neighbour]['weight'] > max_weight:
                max_weight = G[node][neighbour]['weight']
                # max_neighbour = neighbour
        G.nodes[node]['h'] = max_weight
        G.nodes[node]['matched'] = False
    for node in right:
        G.nodes[node]['h'] = 0
        G.nodes[node]['o'] = inf
        G.nodes[node]['matched'] = False


def build_graph(n, m, a, s):
    """
        builds the corresponding complete weighted bipartite graph
    """
    # makes graph complete

    G = nx.complete_bipartite_graph(n, n)

    artificial_nodes = [m + n + i if n > m else n + i for i in range(abs(n-m))]

    for _, (u, v) in enumerate(G.edges()):
        if v in artificial_nodes if n > m else u in artificial_nodes:
            G[u][v]['weight'] = 0
            G[u][v]['artificial'] = True
        else:
            G[u][v]['weight'] = a[u] + s[u][v - n]
            G[u][v]['artificial'] = False
        G[u][v]['matched'] = False

    default_vertex_labeling(G)

    # print("!!!!!!!! G !!!!!!!!")
    # print("NODES")
    # print(G.nodes(data=True))
    # print("EDGES")
    # print(G.edges(data=True))
    # print()

    return G


def build_equality_subgraph(G: nx.Graph):
    """
        builds the corresponding equality subgraph G_h
    """

    G_h = nx.Graph()
    G_h.add_nodes_from(G.nodes(data=True))

    for node in G.nodes():
        for neighbor in G.neighbors(node):
            w = G[node][neighbor]['weight']
            if G.nodes[node]['h'] + G.nodes[neighbor]['h'] == w:
                G_h.add_edge(node, neighbor)
                nx.set_edge_attributes(
                    G_h, {(node, neighbor): G.get_edge_data(node, neighbor)})

    # print("!!!!!!!! G_h !!!!!!!!")
    # print("NODES")
    # print(G_h.nodes(data=True))
    # print("EDGES")
    # print(G_h.edges(data=True))
    # print()

    return G_h


def modify_equality_subgraph(G_h: nx.Graph, G: nx.Graph):

    for edge in G_h.edges():
        u = edge[0]
        v = edge[1]
        w = G[u][v]['weight']
        if G_h.nodes[u]['h'] + G_h.nodes[v]['h'] != w:
            G_h.remove_edge(u, v)

    for node in G_h.nodes():
        G_h.nodes[node]['o'] = inf
        for neighbor in G.neighbors(node):
            w = G[node][neighbor]['weight']
            if G_h.nodes[node]['h'] + G_h.nodes[neighbor]['h'] == w and (node, neighbor) not in G_h.edges():
                G_h.add_edge(node, neighbor)
                nx.set_edge_attributes(
                    G_h, {(node, neighbor): G.get_edge_data(node, neighbor)})

    # print("!!!!!!!! G_h modified !!!!!!!!")
    # print("NODES")
    # print(G_h.nodes(data=True))
    # print("EDGES")
    # print(G_h.edges(data=True))
    # print()


def initial_greedy_bipartite_matching(G_h: nx.Graph):
    """
        gets the initial matching of G_h using greedy tecniche
    """

    M = nx.Graph()

    for node, nodedata in G_h.nodes.items():
        if nodedata['bipartite'] == 0:
            max_weight = -inf
            max_neighbour = 0
            for neighbour in G_h.neighbors(node):
                if not G_h.nodes[neighbour]['matched'] and G_h[node][neighbour]['weight'] > max_weight:
                    max_weight = G_h[node][neighbour]['weight']
                    max_neighbour = neighbour
            if max_weight > -inf:
                G_h.nodes[node]['matched'] = True
                G_h.nodes[max_neighbour]['matched'] = True
                G_h[node][max_neighbour]['matched'] = True

                M.add_nodes_from([(node, nodedata)])
                M.add_nodes_from([(max_neighbour, nodedata)])
                M.add_edge(node, max_neighbour)
                nx.set_edge_attributes(
                    M, {(node, max_neighbour): G_h.get_edge_data(node, max_neighbour)})

    # print("!!!!!!!! M !!!!!!!!")
    # print("NODES")
    # print(M.nodes(data=True))
    # print("EDGES")
    # print(M.edges(data=True))
    # print()

    return M


def symmetric_difference(P: nx.Graph, G_h: nx.Graph):
    """
    Removes M-augmentative path from G_h found in BFS. Symmetric difference between matching M and M-augmentative path P.
    """

    for (u, v) in P.edges():
        if G_h[u][v]['matched']:
            G_h[u][v]['matched'] = False
        else:
            G_h[u][v]['matched'] = True
            G_h.nodes[u]['matched'] = True
            G_h.nodes[v]['matched'] = True

    # print("!!!!!!!! G_h after P !!!!!!!!")
    # print("NODES")
    # print(G_h.nodes(data=True))
    # print("EDGES")
    # print(G_h.edges(data=True))
    # print()


def construct_augmentative_path(d: dict, unmatched_leave):
    """
    Constructs the augmentative path found during BFS through predecesors dictionary.
    """

    P = nx.Graph()
    current = unmatched_leave
    while current != None:
        P.add_node(current)
        predecesor = d[current]
        if predecesor != None:
            P.add_edge(current, predecesor)
        current = predecesor
    return P


def find_augmenting_path(G_h: nx.Graph, G: nx.Graph):
    """
    Finds M-augmenting path in G_h
    """

    Q = []  # inicializar con vertices no emparejados, cada uno de estos vertices en la raiz de un bosque
    F_l = set()
    F_r = set()
    d = {}
    unmatched_leaf = None

    left = []
    right = []
    for node in G_h:
        if G_h.nodes[node]['bipartite'] == 0:
            left.append(node)
            if not G_h.nodes[node]['matched']:
                d[node] = None
                Q.append(node)
                F_l.add(node)
        else:
            right.append(node)

    # set R-F_r
    T = right.copy()
    not_ap = True

    while not_ap:
        # if Q is empty it means that a M-augmenting path was not found in G_h, so the graph has to change
        if len(Q) == 0:

            # delta = min{ l.h + r.l - w(l,r): l in F_l and r in T}
            delta = inf

            # finds delta from attribute sigma of nodes in T
            for r in T:
                temp = G_h.nodes[r]['o']
                if temp < delta and temp > 0:
                    delta = temp

            # update attribute h
            for l in F_l:
                G_h.nodes[l]['h'] = G_h.nodes[l]['h'] - delta
            for r in F_r:
                G_h.nodes[r]['h'] = G_h.nodes[r]['h'] + delta

            # get new egdes of graph G_h
            old_edges = set(G_h.edges())
            modify_equality_subgraph(G_h, G)     # n^2
            new_edges = set(G_h.edges()).difference(old_edges)

            # d = {}
            unmatched_leaf = None

            for node in left:
                if not G_h.nodes[node]["matched"]:
                    Q.append(node)
                    d[node] = None
                    F_l.add(node)

            # set R-F_r
            T = right.copy()

            for (l, r) in new_edges:
                if r not in F_r:
                    d[r] = l
                    if not G_h.nodes[r]['matched']:
                        unmatched_leaf = r
                        not_ap = False
                        break
                    else:
                        Q.append(r)
                        F_r.add(r)
                        T.remove(r)

            # if not not_ap:
            #     break

        u = Q.pop(0)

        #
        if u in right:
            for v in G_h.neighbors(u):
                if G_h[u][v]['matched']:
                    d[v] = u
                    F_l.add(v)
                    Q.append(v)
        # u in left
        else:
            # calculate sigma
            for r in T:
                temp = G_h.nodes[u]['h'] + \
                    G_h.nodes[r]['h'] - G[u][r]['weight']
                if temp < G_h.nodes[r]['o']:
                    G_h.nodes[r]['o'] = temp

            for v in G_h.neighbors(u):
                # if not (G_h.nodes[u]['matched'] or G_h.nodes[v]['matched']):
                #    continue
                if not G_h[u][v]['matched'] and v not in F_r:
                    d[v] = u
                    if not G_h.nodes[v]['matched']:
                        unmatched_leaf = v
                        not_ap = False
                        break
                    else:
                        Q.append(v)
                        F_r.add(v)
                        T.remove(v)

    # P grafito
    P = construct_augmentative_path(d, unmatched_leaf)

    return P


def hungarian_solution(n, m, a, s):
    G = build_graph(n, m, a, s)
    G_h = build_equality_subgraph(G)
    M = initial_greedy_bipartite_matching(G_h)
    # print("!!!!!!!! G_h after M !!!!!!!!")
    # print("NODES")
    # print(G_h.nodes(data=True))
    # print("EDGES")
    # print(G_h.edges(data=True))
    # print()

    matching_cardinality = len(M.edges())
    while matching_cardinality != n:
        # print(matching_cardinality)

        P = find_augmenting_path(G_h, G)
        symmetric_difference(P, G_h)

        matching_cardinality = 0
        for edge in G_h.edges():
            if G_h.edges[edge]['matched']:
                matching_cardinality += 1

    answer = [-1 for i in range(m)]
    max_value = 0
    for node in G_h:
        if G_h.nodes[node]['bipartite'] == 0:
            for neighbor in G_h.neighbors(node):
                if G_h[node][neighbor]['matched'] and not G_h[node][neighbor]['artificial']:
                    answer[neighbor - n] = node
                    max_value += G_h[node][neighbor]['weight']
                    break
    print(answer, max_value)
    return answer, max_value


hungarian_solution(7, 6, [0, 0, 0, 0, 0, 0, 0], [[4, 10, 10, 10, 2, 9], [6, 8, 5, 12, 9, 7], [11, 9, 6, 7, 9, 5], [
                   3, 9, 6, 7, 5, 0], [2, 6, 2, 3, 2, 4], [10, 8, 11, 4, 11, 2], [3, 4, 5, 4, 3, 6]])

hungarian_solution(8, 8, [3, 4, 7, 0, 2, 0, 0, 0], [[4, 4, 8, 5, 12, 9, 7, 2], [0, 4, 11, 6, 7, 9, 5, 15], [3, 6, 7, 5, 0, 7, 8, 3], [
                   6, 4, 1, 2, 3, 2, 4, 2], [23, 4, 10, 8, 4, 11, 2, 11], [23, 4, 10, 8, 4, 11, 2, 11], [23, 4, 10, 8, 4, 11, 2, 11], [3, 7, 8, 5, 4, 3, 6, 8]])

# hungarian_solution(9, 9, [2, 3, 4, 7, 0, 2, 0, 0, 0], [[1, 4, 4, 8, 5, 12, 9, 7, 2], [2, 0, 4, 11, 6, 7, 9, 5, 15], [3, 5, 6, 7, 5, 0, 7, 8, 3], [
#                   4, 6, 4, 1, 2, 3, 2, 4, 2], [5, 23, 4, 10, 8, 4, 11, 2, 11], [6, 23, 4, 10, 8, 4, 11, 2, 11], [7, 23, 4, 10, 8, 4, 11, 2, 11], [8, 3, 7, 8, 5, 4, 3, 6, 8], [9, 3, 7, 8, 5, 4, 3, 6, 8]])

hungarian_solution(4, 4, [0, 0, 0, 0], [[2, 8, 2, 4], [
                   1, 7, 2, 6], [3, 8, 1, 4], [1, 3, 5, 7]])

hungarian_solution(3, 3, [5, 10, 4], [[8, 6, 2], [7, 2, 3], [8, 1, 1]])

hungarian_solution(3, 2, [1, 0, 3], [[8, 6], [7, 2], [8, 1]])

hungarian_solution(7, 7, [0, 0, 0, 0, 0, 0, 0], [[4, 10, 10, 10, 2, 9, 3], [6, 8, 5, 12, 9, 7, 2], [11, 9, 6, 7, 9, 5, 15], [
    3, 9, 6, 7, 5, 6, 3], [2, 6, 5, 3, 2, 4, 2], [10, 8, 11, 4, 11, 2, 11], [3, 4, 5, 4, 3, 6, 8]])

# , "elapsed_time": 0.0023577213287353516, "optimal_solution": [1, 3, 4, 0, 2], "optimal_value": 69}

hungarian_solution(6, 6, [4, 1, 4, 5, 1, 3], [[1, 2, 3, 1, 1, 8], [0, 5, 1, 2, 7, 6], [
                   7, 0, 1, 7, 6, 7], [9, 4, 4, 5, 1, 1], [1, 3, 1, 1, 5, 3], [9, 4, 7, 1, 5, 2]])
