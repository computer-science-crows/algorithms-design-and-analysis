import networkx as nx
from networkx import find_cliques_recursive


def build_graph(n_c, n_e_c, p):
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
            if len(intersection) != 0:
                G.add_edge(i, j)

    print('-------------G-------------')
    print('NODES')
    print(G.nodes(data=True))
    print('---------------------------')
    print('EDGES')
    print(G.edges)
    print('---------------------------')

    return G


def max_independent_set():
    pass


def make_schedule(n_c, n_e_c, p):
    G: nx.Graph = build_graph(n_c, n_e_c, p)
    cliques = list(find_cliques_recursive(G))
    print(f'Maximal cliques: {cliques}')
    
    chosen_cliques = []
    i = 0
    while len(chosen_cliques) < n_c and i < n_c:
        for clique in cliques:
            if all(node not in clique for chosen_clique in chosen_cliques for node in chosen_clique):
                chosen_cliques.append(clique)
                if len(chosen_cliques) == n_c:
                    break
        i += 1

    print(f'Chosen cliques: {chosen_cliques}')

    solution = []

    if len(chosen_cliques) < n_c:
        print('Sorry Kevin, no possible solution.')
        return solution

    for c in chosen_cliques:
        solution.append(G.nodes[c[0]]['proposition'])

    print(f'Solution: {solution}')
    return solution


make_schedule(4, [4, 5, 1, 4], [[12, 14, 28, 29], [17, 23, 12, 21, 1], [22], [26, 25, 17, 1], [
    12], [14, 5, 26, 15], [13, 26, 14, 16, 4], [10], [8, 5, 3, 6, 25], [8], [28, 30, 7, 19, 24]])
