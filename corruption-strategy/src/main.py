from app.generator_relaxed import generator
from app.tester import tester
from app.tools import plot_test_results
from solutions.backtrack_solution import backtrack_solution
from solutions.Ford_Fulkerson_solution_relaxed import test_ff
from solutions.backtrack_solution_relaxed import backtrack_solution_relaxed

# Uncomment lines 12, 15, 16 and 19 as you wish to excecute the desired functions :)

# Generates the number of test cases specified and adds them to test_cases.json
#generator(samples=5)

# Test solution for all tests in test_cases.json
# tester(test_ff)

# Plots each function's results and a comparison of the average elapsed time, and saves the pics in json/tests/plots
# plot_test_results()

# n = 4
# m = 5
# a = [1, 5, 2, 2]
# w = [(1, 3, 4), (1, 4, 4), (3, 4, 5), (3, 2, 2), (4, 2, 2)]
# # sol, val = backtrack_solution(4, 5, [1, 5, 2, 2], [4, 4, 5, 2, 2])
# sol, val = backtrack_solution_relaxed(n, m, a, w)
# print(f"solucion backtrack {sol}")
# print(f'valor backtrack {val}')


n = 4
m = 3
a = [53, 61, 22, 48]
w = [[3, 2, 83], [2, 4, 17], [3, 1, 90]]
c, r, p = backtrack_solution_relaxed(n, m, a, w)
print(f'cities: {c}')
print(f'roads: {r}')
print(f'profit: {p}')


# "n": 5, "m": 4, "a": [10, 67, 31, 12, 62], "w": [[3, 4, 21], [4, 2, 98], [5, 3, 29], [1, 5, 39]], "elapsed_time": 0.000774383544921875, "cities": [1, 3, 4, 5], "roads": [2, 0, 1], "optimal_value": 33
n = 5
m = 4
a = [10, 67, 31, 12, 62]
w = [[3, 4, 21], [4, 2, 98], [5, 3, 29], [1, 5, 39]]
c, r, p = backtrack_solution_relaxed(n, m, a, w)
print(f'cities: {c}')
print(f'roads: {r}')
print(f'profit: {p}')

#"n": 5, "m": 4, "a": [50, 51, 12, 31, 23], "w": [[1, 4, 79], [2, 1, 9], [5, 4, 70], [3, 4, 71]], "elapsed_time": 0.0009076595306396484, "cities": [1, 2, 3, 4, 5], "roads": [1, 0, 3, 2], "optimal_value": 62

n = 5
m = 4
a = [50, 51, 12, 31, 23]
w = [[1, 4, 79], [2, 1, 9], [5, 4, 70], [3, 4, 71]]
c, r, p = backtrack_solution_relaxed(n, m, a, w)
print(f'cities: {c}')
print(f'roads: {r}')
print(f'profit: {p}')