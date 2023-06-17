import pulp
import networkx as nx


def linear_prog_sol(G: nx.Graph):
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
    # print("Maximum Independent Set:")
    for i in V:
        if x[i].value() == 1:
            # print(i)
            solution.append(i)

    return (solution, True) if len(solution) > 0 else (solution, False)
