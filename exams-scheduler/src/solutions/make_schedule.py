import networkx as nx


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

    return G


def make_schedule(k, propositions, solver):
    mis = []
    solution = []
    value = False

    if solver.__name__ == 'genetic_algorithm':
        mis, value = solver(k, propositions)
        solution = mis[:k]

    else:
        G: nx.Graph = build_graph(propositions)

        mis, value = solver(G)

        for vertex in mis[:k]:
            solution.append(G.nodes[vertex]['proposition'])

    if len(mis) < k:
        print('Sorry Kevin, no possible solution :(')
        solution = []
        value = False

    print(f'Solution: {solution}')
    return solution, value
