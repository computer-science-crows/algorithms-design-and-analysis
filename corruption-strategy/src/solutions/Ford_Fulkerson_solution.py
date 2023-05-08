import networkx as nx
from math import inf
import numpy as np


def build_graph(n, m, a, w):
    '''Builds artificial directed graph from cities and roads with a source and a sink'''

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

    print(f'G NODES: {G.nodes(data=True)}')
    print("--------------------------------------")
    print(f'G EDGES: {G.edges(data=True)}')

    return G


def get_residual_graph(G: nx.DiGraph):
    '''Gets residual network from original network'''

    G_r = nx.DiGraph()
    G_r.add_nodes_from(G.nodes(data=True))
    print(G_r.nodes(data=True))

    for edge in G.edges():
        # add edges from G that still have capacity
        u, v = edge[0], edge[1]
        c_r = G[u][v]['capacity'] - G[u][v]['flow']
        if c_r > 0:
            G_r.add_edge(u, v)
            G_r[u][v]['residual_capacity'] = c_r

        # add edges from G that are in the flow with inverse direction
        flow = G[u][v]['flow']
        if flow > 0:
            G_r.add_edge(v, u)
            G_r[v][u]['residual_capacity'] = flow

    print(f'G_r NODES: {G_r.nodes(data=True)}')
    print("--------------------------------------")
    print(f'G_r EDGES: {G_r.edges(data=True)}')

    return G_r


def find_augmenting_path(G_r: nx.DiGraph, s, t):
    '''Finds a path p from the source s to the sink t in the residual network G_r'''

    pi = nx.dfs_predecessors(G_r, s)
    if t not in pi.keys():
        return None

    path = []
    current_node = t

    while current_node != s:
        temp = current_node
        current_node = pi[current_node]
        path.append((current_node, temp))

    return path


def residual_capacity_path(G_r: nx.DiGraph, p):
    '''Calculates the residual capacity of the path p in de residual network G_r'''

    capacity_p = inf

    for (u, v) in p:
        capacity_edge = G_r[u][v]['residual_capacity']

        if capacity_p > capacity_edge:
            capacity_p = capacity_edge

    return capacity_p


def max_flow_min_cut(G: nx.DiGraph):

    G_r = get_residual_graph(G)
    s = 'source'
    t = 'sink'

    p = find_augmenting_path(G_r, s, t)

    while (p != None):
        capacity_p = residual_capacity_path(G_r, p)
        for (u, v) in p:
            try:
                G[u][v]['flow'] = G[u][v]['flow'] + capacity_p
            except:
                G[v][u]['flow'] = G[v][u]['flow'] - capacity_p
        G_r = get_residual_graph(G)
        p = find_augmenting_path(G_r, s, t)

    #
    max_flow = 0

    for v in G.neighbors(s):
        max_flow += G[s][v]['flow']

    return max_flow


def get_minimum_cut(G_r: nx.DiGraph):
    pi = nx.dfs_successors(G_r, 'source')

    pass


G = build_graph(3, 4, [10, 20, 3], [5, 15, 4, 7])
# get_residual_graph(G)

print(f'MAX FLOW: {max_flow_min_cut(G)}')
print()

T = nx.DiGraph()
T.add_nodes_from(['source', 'a', 'b', 'c', 'd', 'e', 'sink'])
T.add_edges_from([('source', 'a'), ('source', 'b'), ('a', 'c'), ('a', 'd'), ('c', 'd'),
                 ('c', 'e'), ('c', 'sink'), ('b', 'c'), ('b', 'e'), ('e', 'sink'), ('d', 'sink')])

T['source']['a']['capacity'] = 40
T['source']['b']['capacity'] = 40
T['a']['c']['capacity'] = 10
T['a']['d']['capacity'] = 10
T['c']['d']['capacity'] = 20
T['c']['e']['capacity'] = 10
T['c']['sink']['capacity'] = 10
T['b']['c']['capacity'] = 15
T['b']['e']['capacity'] = 20
T['e']['sink']['capacity'] = 20
T['d']['sink']['capacity'] = 30


T['source']['a']['flow'] = 0
T['source']['b']['flow'] = 0
T['a']['c']['flow'] = 0
T['a']['d']['flow'] = 0
T['c']['d']['flow'] = 0
T['c']['e']['flow'] = 0
T['c']['sink']['flow'] = 0
T['b']['c']['flow'] = 0
T['b']['e']['flow'] = 0
T['e']['sink']['flow'] = 0
T['d']['sink']['flow'] = 0

print(max_flow_min_cut(T))
# print(nx.dfs_predecessors(T))
