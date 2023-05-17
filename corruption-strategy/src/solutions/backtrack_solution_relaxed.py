import numpy as np


def backtrack_solution_relaxed(n, m, a, w):

    # boolean array to mark selected roads
    cities = [[-1 for i in range(n)] for j in range(n)]

    # list of best assigment of candidates and position
    best_solution = []

    # list of solutions
    answer = []

    _backtrack_solution_relaxed(cities, best_solution, 0, a, w, answer, m)

    value = max(answer)
    solution = best_solution[answer.index(value)]

    return solution[0], solution[1], value


def _backtrack_solution_relaxed(cities, best_solution, count, a, w, answer, m):

    # base case
    if count <= m:
        current_cost, current_cities_selection, current_road_selection = cost(
            cities, a, w, len(a))
        answer.append(current_cost)
        best_solution.append(
            [np.copy(current_cities_selection).tolist(), np.copy(current_road_selection).tolist()])

        if count == len(w):
            return

    # in each iteration one candidate is assign to a position
    for i in range(m):
        city_1, city_2, road_cost = w[i]

        if cities[city_1-1][city_2-1] < 0 and city_1 != city_2:
            cities[city_1-1][city_2-1] = count
            cities[city_2-1][city_1-1] = count
            _backtrack_solution_relaxed(cities, best_solution,
                                        count + 1, a, w, answer, m)
            cities[city_1-1][city_2-1] = -1
            cities[city_2-1][city_1-1] = -1


def cost(cities, a, w, n):

    solution_cost = 0

    mark = [False for i in range(len(a))]
    mark_cities = [[False for i in range(n)] for i in range(n)]

    selected_roads = []
    selected_cities = set()

    for i in range(n):
        for j in range(n):
            road_cost = 0
            if not mark_cities[i][j] and cities[i][j] > 0:
                mark_cities[i][j] = True
                mark_cities[j][i] = True
                city_1, city_2, road = w[cities[i][j]]
                road_cost += road
                if not mark[i]:
                    road_cost -= a[i]
                    mark[i] = True
                if not mark[j]:
                    road_cost -= a[j]
                    mark[j] = True
                solution_cost += road_cost
                selected_roads.append(cities[i][j])
                selected_cities.add(i+1)
                selected_cities.add(j+1)

    return solution_cost, list(selected_cities), selected_roads
