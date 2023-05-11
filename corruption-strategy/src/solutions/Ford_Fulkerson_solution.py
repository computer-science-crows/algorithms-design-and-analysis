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
    for i in range(m):
        G.add_node(i)
        G.add_edge('source', i)
        G['source'][i]['capacity'] = w[i]
        G['source'][i]['flow'] = 0
        G.nodes[i]['type'] = 'road'

    # add artificial node sink
    G.add_node('sink')
    G.nodes['sink']['type'] = 'sink'

    # add road nodes and edges between roads and sink with cost w
    for i in range(m, n+m):
        G.add_node(i)
        G.add_edge(i, "sink")
        G[i]['sink']['capacity'] = a[i-m]
        G[i]['sink']['flow'] = 0
        G.nodes[i]['type'] = 'city'

    # add artificial edges with infinite capacity
    for road in range(m):
        for city in range(m, n+m):
            G.add_edge(road, city)
            G[road][city]['capacity'] = inf
            G[road][city]['flow'] = 0

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

    get_project_distro(G_r, G)
    max_flow = 0

    for v in G.neighbors(s):
        max_flow += G[s][v]['flow']

    return max_flow, G


def get_min_cut(G_r: nx.DiGraph, G: nx.DiGraph):
    s = nx.descendants(G_r, 'source').union(['source'])
    t = set(G.nodes()).difference(s)

    edges_in_cut = []

    cities = []
    roads = [u for u in G.nodes() if G.nodes[u]['type'] == 'road']
    profit = 0

    for u in s:
        for v in t:
            try:
                G[u][v]
                edges_in_cut.append((u, v))
                c = G[u][v]['capacity']

                if G.nodes[u]['type'] == 'city':
                    cities.append(u)
                    profit -= c

                if G.nodes[v]['type'] == 'road':
                    cities.append(v)
                    profit += c

            except:
                continue

    print(f'S: {list(s)}')
    print(f'G: {list(t)}')
    print(f'Edges in MINCUT: {edges_in_cut}')
    print(f'Roads in project: {roads}')
    print(f'Cities in project: {cities}')
    print(f'Profit: {profit}')

    return cities, roads, profit


def get_project_distro(G_r: nx.DiGraph, G: nx.DiGraph):
    cities = []
    roads = []
    profit = 0

    s = nx.descendants(G_r, 'source')
    for u in s:
        try:
            profit += G['source'][u]['capacity']
            roads.append(u)
        except:
            profit -= G[u]['sink']['capacity']
            cities.append(u)

    print(f'Roads in project: {roads}')
    print(f'Cities in project: {cities}')
    print(f'Profit: {profit}')

    return cities, roads, profit


# G = build_graph(4, 3, [5, 15, 4, 7], [10, 20, 3])
# G = build_graph(4, 5, [1, 5, 2, 2], [4, 4, 5, 2, 2])
# get_residual_graph(G)

G = nx.DiGraph()
G.add_nodes_from(['source', 1, 2, 3, 4, 5, 6, 7, 8, 9, 'sink'])
G.add_edges_from([('source', 1), ('source', 2), ('source', 3), ('source', 4), ('source', 5), (1, 6), (1, 8), (2, 6),
                 (2, 9), (3, 8), (3, 9), (4, 7), (4, 8), (5, 7), (5, 9), (9, 'sink'), (6, 'sink'), (7, 'sink'), (8, 'sink')])

G['source'][1]['capacity'] = 4
G['source'][2]['capacity'] = 4
G['source'][3]['capacity'] = 5
G['source'][4]['capacity'] = 2
G['source'][5]['capacity'] = 2
G[1][6]['capacity'] = inf
G[1][8]['capacity'] = inf
G[2][6]['capacity'] = inf
G[2][9]['capacity'] = inf
G[3][8]['capacity'] = inf
G[3][9]['capacity'] = inf
G[4][7]['capacity'] = inf
G[4][8]['capacity'] = inf
G[5][7]['capacity'] = inf
G[5][9]['capacity'] = inf
G[6]['sink']['capacity'] = 1
G[7]['sink']['capacity'] = 5
G[8]['sink']['capacity'] = 2
G[9]['sink']['capacity'] = 2

G['source'][1]['flow'] = 0
G['source'][2]['flow'] = 0
G['source'][3]['flow'] = 0
G['source'][4]['flow'] = 0
G['source'][5]['flow'] = 0
G[1][6]['flow'] = 0
G[1][8]['flow'] = 0
G[2][6]['flow'] = 0
G[2][9]['flow'] = 0
G[3][8]['flow'] = 0
G[3][9]['flow'] = 0
G[4][7]['flow'] = 0
G[4][8]['flow'] = 0
G[5][7]['flow'] = 0
G[5][9]['flow'] = 0
G[6]['sink']['flow'] = 0
G[7]['sink']['flow'] = 0
G[8]['sink']['flow'] = 0
G[9]['sink']['flow'] = 0

G.nodes['source']['type'] = 'source'
G.nodes['sink']['type'] = 'sink'

for i in range(1, 6):
    G.nodes[i]['type'] = 'road'

for i in range(6, 10):
    G.nodes[i]['type'] = 'city'

print(f'G NODES: {G.nodes(data=True)}')
print("--------------------------------------")
print(f'G EDGES: {G.edges(data=True)}')

flow, S = max_flow_min_cut(G)
print(f'MAX FLOW: {flow}')
print()

# T = nx.DiGraph()
# T.add_nodes_from(['source', 'a', 'b', 'c', 'd', 'e', 'sink'])
# T.add_edges_from([('source', 'a'), ('source', 'b'), ('a', 'c'), ('a', 'd'), ('c', 'd'),
#                  ('c', 'e'), ('c', 'sink'), ('b', 'c'), ('b', 'e'), ('e', 'sink'), ('d', 'sink')])

# T['source']['a']['capacity'] = 40
# T['source']['b']['capacity'] = 40
# T['a']['c']['capacity'] = 10
# T['a']['d']['capacity'] = 10
# T['c']['d']['capacity'] = 20
# T['c']['e']['capacity'] = 10
# T['c']['sink']['capacity'] = 10
# T['b']['c']['capacity'] = 15
# T['b']['e']['capacity'] = 20
# T['e']['sink']['capacity'] = 20
# T['d']['sink']['capacity'] = 30


# T['source']['a']['flow'] = 0
# T['source']['b']['flow'] = 0
# T['a']['c']['flow'] = 0
# T['a']['d']['flow'] = 0
# T['c']['d']['flow'] = 0
# T['c']['e']['flow'] = 0
# T['c']['sink']['flow'] = 0
# T['b']['c']['flow'] = 0
# T['b']['e']['flow'] = 0
# T['e']['sink']['flow'] = 0
# T['d']['sink']['flow'] = 0

# print(max_flow_min_cut(T))
# print(nx.dfs_predecessors(T))
