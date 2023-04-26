import networkx as nx
from math import inf
import numpy as np


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

    print(f'G NODES: {G.nodes(data=True)}')
    print("--------------------------------------")
    print(f'G EDGES: {G.edges(data=True)}')

    return G


def get_residual_graph(G: nx.DiGraph):
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


def max_flow_min_cut(G: nx.Graph, G_r,s,t):

    p = path_ff(G_r,s,t)
    while (p != None):
        capacity_p = capacity(G_r,p)
        for (u,v) in p:
            if (u,v) in G.edges():
                G[u][v]['flow'] = G[u][v]['flow'] + capacity_p
            else:
                G[v][u]['flow'] = G[v][u]['flow'] - capacity_p
            G_r= get_residual_graph(G)

            
def path_ff(G,s,t):
    pi = nx.dfs_predecessors(G,s)
    if pi[t] == None:
        return None
    
    path = []
    current_node = s

    while current_node != t:
        temp = np.copy(current_node)
        current_node = pi[current_node]
        path.append((temp,current_node))       
    

    return path

def capacity(G, p):

    capacity_p = -inf

    for (u,v) in p: 
        capacity_edge = 0
        if (u,v) in G.edges:
            capacity_edge = G[u][v]['capacity'] - G[u][v]['flow']
        elif (v,u) in G.edges:
            capacity_edge = G[v][u]['flow']
        
        if capacity_p > capacity_edge:
            capacity_p = capacity_edge

    return capacity_p


            
    






G = build_graph(4, 3, [1, 2, 3, 4], [5, 6, 7, 8])
get_residual_graph(G)
