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

    return G_r

def max_flow_min_cut(G: nx.DiGraph):

    G_r = get_residual_graph(G)
    s= 'source'
    t='sink'

    p = path_ff(G_r,s,t)

    edges = G.edges()

    while (p != None):
        capacity_p = residual_capacity_path(G_r,p)
        for (u,v) in p:
            try:
                G[u][v]['flow'] = G[u][v]['flow'] + capacity_p
            except:
                G[v][u]['flow'] = G[v][u]['flow'] - capacity_p
        G_r= get_residual_graph(G)
        p = path_ff(G_r,s,t)

    max_flow = 0

    for v in G.neighbors(t):
        max_flow += G[v][t]['flow']

    return max_flow

def dfs(G:nx.DiGraph):

    pi = {}
    visited = {}

    for u in G.nodes:
        visited[u] = False
        pi[u]=None

    for u in G.nodes:
        if not visited[u]:
            visited[u]=True
            visited,pi, visit_t = dfs_visit(G,u, visited,pi)

    return pi


def dfs_visit(G:nx.DiGraph,u, visited, pi):

    visit_t = False
    for v in G.neighbors(u):
        if not visited[v]:
            pi[v]=u
            
            visited,pi, visit_t = dfs_visit(G,v,visited,pi)
        

    return visited,pi, visit_t


def path_ff(G: nx.DiGraph,s,t):

    '''Finds a path p from the source s to the sink t in the residual network G_r'''

    pi = nx.dfs_predecessors(G,s)
    if t not in pi.keys():
        return None
    
    path = []
    current_node = t

    while current_node != s:
        temp = current_node
        current_node = pi[current_node]
        path.append((current_node,temp))   
    
    return path

def residual_capacity_path(G_r, p):

    '''Calculates the residual capacity of the path p in de residual network G_r'''

    capacity_p = inf

    for (u,v) in p:               
        capacity_edge = G_r[u][v]['residual_capacity']         
        
        if capacity_p > capacity_edge:
            capacity_p = capacity_edge

    return capacity_p


G = build_graph(4, 3, [1, 2, 3, 4], [5, 6, 7, 8])
#get_residual_graph(G)

print(max_flow_min_cut(G))
