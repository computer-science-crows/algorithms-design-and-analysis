import numpy as np


def backtrack_solution_relaxed(n, m, a, w):

    # boolean array to mark selected roads
    roads = [False for i in range(m)]

    # list of best assigment of candidates and position
    best_solution = []

    # list of solutions
    answer = []

    _backtrack_solution_relaxed(roads, best_solution, 0, a, w, answer, m)

    value = max(answer)
    solution = best_solution[answer.index(value)]

    return solution[0], solution[1], value


def _backtrack_solution_relaxed(roads, best_solution, count, a, w, answer, m):

    # base case
    if count <= m:
        current_cost, current_cities_selection, current_road_selection = cost(
            roads, a, w, len(w))
        answer.append(current_cost)
        best_solution.append(
            [np.copy(current_cities_selection).tolist(), np.copy(current_road_selection).tolist()])

        if count == len(w):
            return

    # in each iteration one candidate is assign to a position
    for i in range(m):
        city_1, city_2, road_cost = w[i]

        if not roads[i]:
            roads[i] = True
            _backtrack_solution_relaxed(roads, best_solution,
                                        count + 1, a, w, answer, m)
            roads[i]= False
            
            


def cost(roads, a, w, m):

    solution_cost = 0

    mark = [False for i in range(len(a))]
   
    selected_roads = []
    selected_cities = set()


    for i in range(m):
        road_cost = 0
        if roads[i]:
            city_1, city_2, road = w[i]
            road_cost += road
            if not mark[city_1-1]:
                road_cost -= a[city_1-1]
                mark[city_1-1] = True
            if not mark[city_2-1]:
                road_cost -= a[city_2-1]
                mark[city_2-1] = True
            solution_cost += road_cost
            selected_roads.append(i+1)
            selected_cities.add(city_1)
            selected_cities.add(city_2)


    return solution_cost, list(selected_cities), selected_roads
