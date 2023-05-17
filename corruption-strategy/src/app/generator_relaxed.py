import numpy as np
import os
import random
from solutions.backtrack_solution import backtrack_solution
import json
from app.tools import save_data
import time


def generator(n=None, m=None, a=None, w=None, samples=1):
    i = 0

    while i < samples:
        if n == None:
            n = random.randint(2, 11) # max es 5
        if m == None:
            m = random.randint(1, 11)

        a = [random.randint(0, 100) for i in range(n)]
        w = []

        while len(w) != m:
            city_1= random.randint(0, 100)
            city_2= random.randint(0, 100)
            road_cost = random.randint(0, 100)

            if (city_1, city_2, road_cost) in w or (city_2,city_1,road_cost) in w or city_1 == city_2:
                continue

            w.append(((city_1, city_2, road_cost)))

       

        start = time.time()
        solution, value = backtrack_solution(n, m, a, w)
        end = time.time()
        print(f'time:{end-start}')
        i += 1

        data = {"n": n, "m": m, "a": a, "w": w, 'elapsed_time': end - start,
                "optimal_solution": solution, "optimal_value": value}

        save_data(data, "/test_cases.json")

        n = None
        m = None