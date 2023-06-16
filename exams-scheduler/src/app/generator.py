import random
from solutions.backtrack_solution import backtrack_solution
from app.tools import save_data
import time


def get_exam_day(c_k, n):
    c_day = random.randint(1, n)
    while c_day in c_k:
        c_day = random.randint(1, n)
    return c_day


def generator(k=None, propositions=None, n=None, samples=1):
    i = 0

    while i < samples:
        if k == None:       # number of courses
            k = random.randint(2, 6)
        if n == None:       # number of days of semester
            n = random.randint(40, 80)

        # number of exams per course
        e = [random.randint(1, 5) for i in range(k)]

        # number of propositions
        n_propositions = random.randint(k, 20)

        # propositions
        propositions = [[]for i in range(n_propositions)]

        for q in range(k):
            for n_ex in range(e[q]):
                propositions[q].append(get_exam_day(propositions[q], n))

        for q in range(k, n_propositions):
            for n_ex in range(random.choice(e)):
                propositions[q].append(get_exam_day(propositions[q], n))

        print(k)
        print(e)
        print(propositions)

        start = time.time()
        solution, value = backtrack_solution(k, propositions)
        end = time.time()
        print(f'time:{end-start}')
        i += 1
        print(f'ITERATION: {i}')
        data = {"k": k, "propositions": propositions, 'elapsed_time': end - start,
                "optimal_solution": solution, "optimal_value": value}

        save_data(data, "/test_cases.json")

        k = None
        e = None
