import networkx as nx
from math import inf


def build_graph(n, m, a, w):
    G = nx.DiGraph()

    # add artificial node source
    G.add_node('source')
    G.nodes['source']['type'] = 'source'

    # add city nodes and edges between source and cities with revenue a
    for i in range(n):
        G.add_node(i)
        G.add_edge('source', i)
        G['source'][i]['capacity'] = a[i]
        G['source'][i]['flow'] = 0
        G.nodes[i]['type'] = 'city'

    # add artificial node sink
    G.add_node('sink')
    G.nodes['sink']['type'] = 'sink'

    # add road nodes and edges between roads and sink with cost w
    for i in range(n, n+m):
        G.add_node(i)
        G.add_edge(i, "sink")
        G[i]['sink']['capacity'] = w[i-n]
        G[i]['sink']['flow'] = 0
        G.nodes[i]['type'] = 'road'

    # add artificial edges with infinite capacity
    for city in range(n):
        for road in range(n, n+m):
            G.add_edge(city, road)
            G[city][road]['capacity'] = inf
            G[city][road]['flow'] = 0

    print(f'G initial NODES: {G.nodes(data=True)}')
    print("--------------------------------------")
    print(f'G initial EDGES: {G.edges(data=True)}')

    return G


def build_residual_graph(G: nx.DiGraph):
    pass


def max_flow_min_cut():
    pass


build_graph(4, 3, [1, 2, 3, 4], [5, 6, 7, 8])
