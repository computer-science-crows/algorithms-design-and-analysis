import networkx as nx
from math import inf


def build_graph(n: int, m: int, a: list, w: list):
    '''Builds artificial directed graph from cities and roads with a source and a sink'''

    G = nx.DiGraph()

    # add artificial node source
    G.add_node('source')
    G.nodes['source']['type'] = 'source'

    # add road nodes and edges between roads and sink with cost w
    for i in range(1, m+1):
        G.add_node(i)
        G.add_edge('source', i)
        G['source'][i]['capacity'] = w[i-1][2]
        G['source'][i]['flow'] = 0
        G.nodes[i]['type'] = 'road'

    # add artificial node sink
    G.add_node('sink')
    G.nodes['sink']['type'] = 'sink'

    # add city nodes and edges between source and cities with revenue a
    for i in range(m+1, n+m+1):
        G.add_node(i)
        G.add_edge(i, "sink")
        G[i]['sink']['capacity'] = a[i-m-1]
        G[i]['sink']['flow'] = 0
        G.nodes[i]['type'] = 'city'

    # add artificial edges with infinite capacity
    for i in range(m):
        city_1 = w[i][0] + m
        city_2 = w[i][1] + m
        road = i + 1

        G.add_edge(road, city_1)
        G[road][city_1]['capacity'] = inf
        G[road][city_1]['flow'] = 0

        G.add_edge(road, city_2)
        G[road][city_2]['capacity'] = inf
        G[road][city_2]['flow'] = 0

    # print(f'G NODES: {G.nodes(data=True)}')
    # print("--------------------------------------")
    # print(f'G EDGES: {G.edges(data=True)}')

    return G


def get_residual_graph(G: nx.DiGraph):
    '''Gets residual network from original network'''

    G_r = nx.DiGraph()
    G_r.add_nodes_from(G.nodes(data=True))
    # print(G_r.nodes(data=True))

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

    # print(f'G_r NODES: {G_r.nodes(data=True)}')
    # print("--------------------------------------")
    # print(f'G_r EDGES: {G_r.edges(data=True)}')

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


def get_project_distro(G_r: nx.DiGraph, G: nx.DiGraph):
    ''' Gets best project distribution from the last residual graph. Returns empty solution in case there is no possible profit'''

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

    # print(f'Roads in project: {roads}')
    # print(f'Cities in project: {cities}')
    # print(f'Profit: {profit}')

    return cities, roads, profit


def get_min_cut_residual_graph(G: nx.DiGraph):
    ''' Gets the last residual graph built by the Ford Fulkerson algorithm'''

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

    return G_r


def corruption_strategy(n, m, a, w):
    ''' Finds best distribution so that Tito can work his magic'''

    G = build_graph(n, m, a, w)
    G_r = get_min_cut_residual_graph(G)
    cities, roads, profit = get_project_distro(G_r, G)
    return cities, roads, profit
