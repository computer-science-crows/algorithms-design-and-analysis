import numpy as np
import os
import random
from solutions.backtrack_solution import backtrack_solution
import json
from app.tools import save_data
import time


def generator(n=None, k=None, p=None, samples=1):
    i = 0

    while i < samples:
        if p == None:
            p = random.randint(1, 10)
        if k == None:
            k = random.randint(0, 10-p)
        if n == None:
            n = random.randint(p+k, 10)

        a = [random.randint(0, 10) for i in range(n)]
        s = np.random.randint(low=0, high=10, size=(n, p+k))
        s = s.tolist()

        start = time.time()
        solution, value = backtrack_solution(n, p+k, a, s)
        end = time.time()
        print(f'time:{end-start}')
        i += 1

        data = {"n": n, "p": p, "k": k, "a": a, "s": s, 'elapsed_time': end - start,
                "optimal_solution": solution, "optimal_value": value}

        save_data(data, "/test_cases.json")

        return n,p,k,a,s,solution,value
        
        p=None
        k=None
        n=None

        

