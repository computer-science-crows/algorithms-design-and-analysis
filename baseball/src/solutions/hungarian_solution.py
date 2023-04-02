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


def exists_M_augmentating_path(G_M_h: nx.Graph):
    Q = [] # inicializar con vertices no emparejados, cada uno de estos vertices en la raiz de un bosque
    F_l = set()
    F_r = set()
    d={}
    
    left, right = nx.bipartite.sets(G_M_h)

    for node in left:
        if not G_M_h.nodes[node]['matched']:
            d[node]= None
            Q.append(node)
            F_l.add(node)

            if not Q:
                delta = search_min(F_l)
                for l in F_l:
                    G_M_h.nodes[l]['h'] = G_M_h.nodes[l]['h'] - delta
                for r in F_r:
                    G_M_h.nodes[r]['h'] = G_M_h.nodes[r]['h'] + delta

                G_M_h, new_edges = modify_graph()

                for (l,r) in new_edges:
                    if r not in F_r:
                        d[r] = l
                        if G_M_h[r]['matches']:
                            break
                        else:
                            Q.append(r)
                            F_r.add(r)
        u = Q.pop()
        for v in  G_M_h.neighbors(u):
            if v in left:
                d[v]=u
                F_l.add(v)
                Q.append(v)
            elif v not in F_r:
                d[v] = u
                if G_M_h[v]['matched']:
                    break
                else:
                    Q.append(v)
                    F_r.add(v)

    P = construct_augmentative_path(d)

    return P


                

# O(n)
def search_min(F_l, R_F_r):
    pass

# se crea un nuevo emparejamiento tomendo la diferencia simetrica del emparejamiento M con el camino M-aumentativo encontrado.
def modify_graph():
    pass

def construct_augmentative_path(d):
    pass


def hungarian_solution(n, m, a, s):
    B = build_graph(n, m, a, s)
    initial_greedy_bipartite_matching(B)
    pass


hungarian_solution(5, 5, [0, 0, 0, 0, 0], [[0, 1, 3, 5, 7], [0, 0, 89, 0, 0], [
    2, 0, 21, 0, 0], [0, 0, 0, 23, 0], [0, 5, 0, 0, 0]])
