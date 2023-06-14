import networkx as nx
from networkx import find_cliques_recursive
import random


def build_graph(p):
    G = nx.Graph()

    for i in range(len(p)):
        G.add_node(i)
        prop = p[i]
        G.nodes[i]['proposition'] = prop
        G.nodes[i]['exams_number'] = len(prop)

    for i in range(len(p) - 1):
        for j in range(1, len(p)):
            intersection = set(G.nodes[i]['proposition']).intersection(
                set(G.nodes[j]['proposition']))
            if len(intersection) != 0 and i != j:
                G.add_edge(i, j)

    print('-------------G-------------')
    print('NODES')
    print(G.nodes())
    print('---------------------------')
    print('EDGES')
    print(G.edges)
    print('---------------------------')

    return G


def make_schedule(n_c, p, solver):
    G: nx.Graph = build_graph(p)

    solution = []

    # TODO: method selection

    if len(solution) == 0:
        print('Sorry Kevin, no possible solution :(')
    print(f'Solution: {solution}')

    return solution


make_schedule(4, [4, 5, 1, 4], [[12, 14, 28, 29], [17, 23, 12, 21, 1], [22], [26, 25, 17, 1], [
    12], [14, 5, 26, 15], [13, 26, 14, 16, 4], [10], [8, 5, 3, 6, 25], [8], [28, 30, 7, 19, 24]])
