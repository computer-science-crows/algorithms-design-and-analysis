import numpy as np


def backtrack_solution(n, m, a, w):

    # boolean array to mark selected roads
    cities = [[-1 for i in range(n)] for j in range(n)]

    # list of best assigment of candidates and position
    best_solution = []

    # list of solutions
    answer = []

    _backtrack_solution(cities, best_solution, 0, a, w, answer, n)

    value = max(answer)
    solution = best_solution[answer.index(value)]

    return solution.tolist(), value


def _backtrack_solution(cities, best_solution, count, a, w, answer, n):

    # base case
    if count <= len(w):
        current_cost, current_road_selection = cost(cities, a, w, n)
        answer.append(current_cost)
        best_solution.append(np.copy(current_road_selection))

        if count == len(w):
            return

    # in each iteration one candidate is assign to a position
    for i in range(n):
        for j in range(n):
            if cities[i][j] < 0 and i != j:
                cities[i][j] = count
                cities[j][i] = count
                _backtrack_solution(cities, best_solution,
                                    count + 1, a, w, answer, n)
                cities[i][j] = -1
                cities[j][i] = -1


def cost(cities, a, w, n):

    solution = []
    solution_cost = 0

    mark = [False for i in range(len(a))]
    mark_cities = [[False for i in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            road_cost = 0
            if not mark_cities[i][j] and cities[i][j] > -1:
                mark_cities[i][j] = True
                mark_cities[j][i] = True
                road_cost += w[cities[i][j]]
                if not mark[i]:
                    road_cost -= a[i]
                    mark[i] = True
                if not mark[j]:
                    road_cost -= a[j]
                    mark[j] = True
                solution_cost += road_cost
                solution.append((i, j, cities[i][j]))

    return solution_cost, solution
