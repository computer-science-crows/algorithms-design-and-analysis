import random


def randomized_mis(G):
    S = set()
    vertices = list(G.nodes())
    random.shuffle(vertices)
    for v in vertices:
        if all(u not in S for u in G.neighbors(v)):
            S.add(v)
    return S
