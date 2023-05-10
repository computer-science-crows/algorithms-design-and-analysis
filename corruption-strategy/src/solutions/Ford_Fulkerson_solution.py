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
    for city in range(m):
        for road in range(m, n+m):
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

def dfs(G: nx.DiGraph):
    
    pi = {}
    visited = {}
    CC = {}
    i = 1

    for v in G.nodes():
        pi[v] = inf
        visited[v]=False
        CC[v] = -1

    for v in G.nodes():
        if not visited[v]:
            dfs_visit(G,v, visited, pi, CC, i)
            i+=1

    print(f'PI {pi}')
    print(f'visited {visited}')
    print(f'CC {CC}')

    return CC

def dfs_visit(G: nx.DiGraph,u, visited, pi, CC, i):
    visited[u] = True

    for v in G.neighbors(u):
        if not visited[v]:
            pi[v] = u
            dfs_visit(G,v,visited,pi, CC, i)
    CC[u] = i
    
    

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

    dfs(G)
    min_cut(G, G_r)

    return max_flow


def get_project_distro(G: nx.DiGraph):
    cities = []
    roads = []
    value = 0

    for edge in G.edges():
        u, v = edge[0], edge[1]
        c = G[u][v]['capacity']
        if c != inf:
            f = G[u][v]['flow']
            if c == f:
                if G.nodes[v]['type'] == 'city':
                    cities.append(v)
                    value += c
                # if G.nodes[u]['type'] == 'road':
                #     roads.append(u)
            else:
                if G.nodes[u]['type'] == 'road':
                    roads.append(u)
                    value -= c

    return cities, roads, value

def min_cut(G: nx.DiGraph, G_r: nx.DiGraph):

    
    # Falta verificar si alguna arista de costo inf se corto
    print(f'G_r edges min cut: {G_r.edges(data=True)}')
    print(f'G edges min cut: {G.edges(data=True)}')
    CC = dfs(G)
    
    s =set()
    roads = set()
    cities = set()
    profit = 0
    

    for key in CC.keys():
        if CC[key] == 1:
            s.add(key)
        

    print(f'S {list(s)}')

    for v in s:
        if G.nodes[v]['type'] == 'road':
            roads.add(v)
            profit += G['source'][v]['capacity']

        if G.nodes[v]['type'] == 'city':
            cities.add(v)
            profit -= G[v]['sink']['capacity']

    print(f'Profit {profit}')
    print(f'Road {list(roads)}')
    print(f'Cities {list(cities)}')
    

    return profit, roads, cities








    



G = build_graph(4,5,[1,5,2,2],[4,4,5,2,2])
# get_residual_graph(G)
print(f'MAX FLOW: {max_flow_min_cut(G)}')
print()

#D = nx.DiGraph()
#
#D.add_nodes_from(['source', '1', '2', '3', '4', 'sink'])
#D.add_edges_from([('source', '1'), ('source', '2'), ('1', '3'), ('2', '4'), ('2', '1'),('3', '2'), ('3', 'sink'), ('4', '3'),  ('4', 'sink')])
#
#
#D['source']['1']['capacity'] = 16
#D['source']['2']['capacity'] = 13
#D['1']['3']['capacity'] = 12
#D['2']['4']['capacity'] = 14
#D['2']['1']['capacity'] = 4
#D['3']['2']['capacity'] = 9
#D['3']['sink']['capacity'] = 20
#D['4']['3']['capacity'] = 7
#D['4']['sink']['capacity'] = 4
#
#D['source']['1']['flow'] = 0
#D['source']['2']['flow'] = 0
#D['1']['3']['flow'] = 0
#D['2']['4']['flow'] = 0
#D['2']['1']['flow'] = 0
#D['3']['2']['flow'] = 0
#D['3']['sink']['flow'] = 0
#D['4']['3']['flow'] = 0
#D['4']['sink']['flow'] = 0
#
#
#print(f'flow {max_flow_min_cut(D)}')

#T = nx.DiGraph()
#T.add_nodes_from(['source', 'a', 'b', 'c', 'd', 'e', 'sink'])
#T.add_edges_from([('source', 'a'), ('source', 'b'), ('a', 'c'), ('a', 'd'), ('c', 'd'),
#                 ('c', 'e'), ('c', 'sink'), ('b', 'c'), ('b', 'e'), ('e', 'sink'), ('d', 'sink')])
#
#T['source']['a']['capacity'] = 40
#T['source']['b']['capacity'] = 40
#T['a']['c']['capacity'] = 10
#T['a']['d']['capacity'] = 10
#T['c']['d']['capacity'] = 20
#T['c']['e']['capacity'] = 10
#T['c']['sink']['capacity'] = 10
#T['b']['c']['capacity'] = 15
#T['b']['e']['capacity'] = 20
#T['e']['sink']['capacity'] = 20
#T['d']['sink']['capacity'] = 30
#
#
#T['source']['a']['flow'] = 0
#T['source']['b']['flow'] = 0
#T['a']['c']['flow'] = 0
#T['a']['d']['flow'] = 0
#T['c']['d']['flow'] = 0
#T['c']['e']['flow'] = 0
#T['c']['sink']['flow'] = 0
#T['b']['c']['flow'] = 0
#T['b']['e']['flow'] = 0
#T['e']['sink']['flow'] = 0
#T['d']['sink']['flow'] = 0
#
#print(max_flow_min_cut(T))
# print(nx.dfs_predecessors(T))
