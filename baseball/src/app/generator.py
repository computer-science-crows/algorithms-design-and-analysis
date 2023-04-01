import numpy as np
import os
import random
# from solutions.backtrack_solution import backtrack_solution
import json
from tools import save_data
# from visualiser.visualiser import Visualiser as vs


def generator(n=None, k=None, p=None, samples=1):
    i = 0

    while i < samples:
        if n == None:
            n = random.randint(0, 20)
        if k == None:
            k = random.randint(0, 20)
        if p == None:
            p = random.randint(0, 20)

        a = [random.randint(0, 10) for i in range(n)]
        s = np.random.randint(low=0, high=10, size=(n, p+k))
        s = s.tolist()
        solution = 0
        # solution = backtrack_solution(n,p,k,a,s)
        # vs.make_animation("backtrack_solution.gif", delay=2)
        i += 1

        data = {"n": n, "p": p, "k": k, "a": a, "s": s,
                "optimal_solution": solution}

        save_data(data, "/test_cases.json")

        return n, p, k, a, s, solution


print(generator())
