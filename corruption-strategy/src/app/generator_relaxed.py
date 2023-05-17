import random
from solutions.backtrack_solution_relaxed import backtrack_solution_relaxed
from app.tools import save_data
import time


def generator_relaxed(n=None, m=None, a=None, w=None, samples=1):
    i = 0

    while i < samples:
        if n == None:
            n = random.randint(2, 5)
        if m == None:
            m = random.randint(1, min(int(n * (n-1) / 2), 5))

        a = [random.randint(0, 100) for i in range(n)]
        w = []

        roads = []
        while len(w) != m:
            city_1 = random.randint(1, n)
            city_2 = random.randint(1, n)
            road_cost = random.randint(0, 100)

            if (city_1, city_2) in roads or (city_2, city_1) in roads or city_1 == city_2:
                continue

            roads.append((city_1, city_2))

            w.append((city_1, city_2, road_cost))

        start = time.time()
        cities, roads, profit = backtrack_solution_relaxed(n, m, a, w)
        end = time.time()
        print(f'time:{end-start}')

        if profit != 0:
            i += 1

            data = {"n": n, "m": m, "a": a, "w": w, 'elapsed_time': end - start,
                    "cities": cities, "roads": roads, "optimal_value": profit}

            save_data(data, "/test_cases_relaxed.json")

        n = None
        m = None
