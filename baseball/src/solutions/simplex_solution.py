from scipy.optimize import linprog
import numpy as np

# TODO comentar


def simplex_solution(n, m, a, s):

    objective_function = [-(s[i][j] + a[i])
                          for i in range(n) for j in range(m)]

    A_eq, b_eq = constrains(n, m)

    solution = linprog(objective_function, A_eq=A_eq,
                       b_eq=b_eq, bounds=None, method='simplex')

    return solution.x, solution.fun


def constrains(n, m):

    A_eq = []
    b_eq = [1 for i in range(n+m)]

    ones = [1 for i in range(m)]

    for i in range(n):
        temp = [0 for j in range(n*m)]
        temp[i*m:i*m + m] = ones
        A_eq.append(temp)

    for i in range(m):
        temp = [0 for j in range(n*m)]
        for j in range(n):
            temp[j*m+i] = 1
        A_eq.append(temp)

    return np.array(A_eq), np.array(b_eq)
