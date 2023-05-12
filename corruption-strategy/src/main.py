from app.generator_relaxed import generator
from app.tester import tester
from app.tools import plot_test_results
from solutions.backtrack_solution import backtrack_solution
from solutions.Ford_Fulkerson_solution_relaxed import test_ff
from solutions.backtrack_solution_relaxed import backtrack_solution_relaxed

# Uncomment lines 12, 15, 16 and 19 as you wish to excecute the desired functions :)

# Generates the number of test cases specified and adds them to test_cases.json
generator(samples=5)

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
