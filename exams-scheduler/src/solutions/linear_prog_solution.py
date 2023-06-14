import pulp
import networkx as nx


def linear_prog_sol(G: nx.Graph, k=None):
    V = G.nodes()
    E = G.edges()

    # create the LP problem
    prob = pulp.LpProblem("Maximum Independent Set", pulp.LpMaximize)

    # create the binary variables
    x = pulp.LpVariable.dicts("x", V, cat=pulp.LpBinary)

    # set the objective function
    prob += pulp.lpSum([x[i] for i in V])

    # add the constraints
    for (i, j) in E:
        prob += x[i] + x[j] <= 1

    # solve the LP problem
    prob.solve()

    solution = []
    print("Maximum Independent Set:")
    for i in V:
        if x[i].value() == 1:
            print(i)
            solution.append(i)

    return solution if k == None else [] if k > len(solution) else solution[:k]


# Define the graph
V = range(0, 11)
E = [(0, 1), (0, 4), (0, 5), (0, 6), (0, 10), (1, 3),
     (1, 4), (3, 5), (3, 6), (3, 8), (5, 6), (5, 8), (8, 9)]

print(linear_prog_sol(V, E, 5))
