import pulp


def simplex_sol(V, E, k=None):
    # Create the LP problem
    prob = pulp.LpProblem("Maximum Independent Set", pulp.LpMaximize)

    # Create the binary variables
    x = pulp.LpVariable.dicts("x", V, cat=pulp.LpBinary)

    # Set the objective function
    prob += pulp.lpSum([x[i] for i in V])

    # Add the constraints
    for (i, j) in E:
        prob += x[i] + x[j] <= 1

    # Solve the LP problem
    prob.solve()

    solution = []
    # Print the solution
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

print(simplex_sol(V, E, 5))
