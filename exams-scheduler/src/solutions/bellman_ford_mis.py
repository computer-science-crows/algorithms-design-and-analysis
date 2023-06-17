import networkx as nx
from math import inf


def BMA(G: nx.Graph):
    exclude = {}
    cost = {}
    previous = {}

    for u in G.nodes:
        exclude[f'({u},{0})'] = set()
        exclude[f'({u},{0})'].add(u)
        cost[f'({u},{0})'] = 1
        previous[f'({u},{0})'] = None

        for v in G.neighbors(u):
            exclude[f'({u},{0})'].add(v)
            cost[f'({u},{0})'] += 1
        for round in range(1, len(G.nodes)):
            previous[f'({u},{round})'] = None
            cost[f'({u},{round})'] = inf

    last_round = 0
    last_vertex = None

    for round in range(0, len(G.nodes)-1):
        change_cost = False

        for u in G.nodes:
            try:
                not_adjacent_nodes = set(G.nodes).difference(
                    set(exclude[f'({u},{round})']))
            except:
                continue
            for v in not_adjacent_nodes:
                v_exclude = set()
                v_cost = 0
                if cost[f'({u},{round})'] < inf:
                    v_exclude.update(exclude[f'({u},{round})'])
                    v_exclude.add(v)
                    v_cost += 1 + cost[f'({u},{round})']

                    for j in G.neighbors(v):
                        if j not in v_exclude:
                            v_exclude.add(j)
                            v_cost += 1

                    if cost[f'({v},{round + 1})'] > v_cost:
                        previous[f'({v},{round + 1})'] = u
                        exclude[f'({v},{round + 1})'] = v_exclude
                        cost[f'({v},{round+1})'] = v_cost

                        change_cost = True
                        last_vertex = v

        if not change_cost:
            last_round = round
            break

    t = last_vertex
    independent_set = set()
    independent_set.add(t)

    while t != None:

        t = previous[f'({t},{last_round})']
        if t != None:
            independent_set.add(t)
        last_round -= 1

    print(f"independent_set {independent_set}")
    return independent_set


def bellman_ford_mis(G):
    independent_sets = list(BMA(G))
    value = False

    if len(independent_sets) > 0 and independent_sets[0] != None:
        value = True
    else:
        independent_sets = []

    return independent_sets, value