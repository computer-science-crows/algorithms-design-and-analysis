def greedy_mis(G):
    S = set()
    for v in G.nodes():
        if all(u not in S for u in G.neighbors(v)):
            S.add(v)
    return S
