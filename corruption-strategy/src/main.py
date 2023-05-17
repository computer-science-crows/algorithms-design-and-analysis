from app.generator import generator
from app.tester import tester
from app.tools import plot_test_results
from solutions.backtrack_solution import backtrack_solution
<<<<<<< Updated upstream
from solutions.Ford_Fulkerson_solution import max_flow_min_cut

=======
from solutions.Ford_Fulkerson_solution_relaxed import corruption_strategy
from solutions.backtrack_solution_relaxed import backtrack_solution_relaxed
>>>>>>> Stashed changes

# Uncomment lines 12, 15, 16 and 19 as you wish to excecute the desired functions :)

# Generates the number of test cases specified and adds them to test_cases.json
<<<<<<< Updated upstream
# generator(samples=1)

# Test solution for all tests in test_cases.json
# tester(simplex_solution)
# tester(hungarian_solution)
=======
# generator(samples=3000)

# Test solution for all tests in test_cases.json
# tester(corruption_strategy)
>>>>>>> Stashed changes

# Plots each function's results and a comparison of the average elapsed time, and saves the pics in json/tests/plots
# plot_test_results()

<<<<<<< Updated upstream
sol, val = backtrack_solution(3,4,[-10,-20,-3],[-5,-15,-4,-7])
flujo = 
print(f"solucion backtrack {sol}")
print(f'valor backtrack {val}')
=======
# n = 4
# m = 5
# a = [1, 5, 2, 2]
# w = [(1, 3, 4), (1, 4, 4), (3, 4, 5), (3, 2, 2), (4, 2, 2)]
# # sol, val = backtrack_solution(4, 5, [1, 5, 2, 2], [4, 4, 5, 2, 2])
# sol, val = backtrack_solution_relaxed(n, m, a, w)
# print(f"solucion backtrack {sol}")
# print(f'valor backtrack {val}')

# n = 4
# m = 3
# a = [53, 61, 22, 48]
# w = [[3, 2, 83], [2, 4, 17], [3, 1, 90]]
# c, r, p = backtrack_solution_relaxed(n, m, a, w)
# print(f'cities: {c}')
# print(f'roads: {r}')
# print(f'profit: {p}')

# "elapsed_time": 0.00015854835510253906, "cities": [1, 3], "roads": [0], "optimal_value": 8}
>>>>>>> Stashed changes
