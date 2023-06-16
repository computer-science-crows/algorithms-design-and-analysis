from app.generator import generator
from app.tester import tester
from app.tools import plot_test_results
from solutions.backtrack_solution import backtrack_solution
from solutions.linear_prog_solution import linear_prog_sol
from solutions.genetic_algorithm import genetic_algorithm
from solutions.bellman_ford_mis import bellman_ford_mis
from solutions.make_schedule import make_schedule

# Uncomment lines 11, 14 and 17 as you wish to excecute the desired functions :)

# Generates the number of test cases specified and adds them to test_cases.json
# generator(samples=3000)

# Test solution for all tests in test_cases.json
tester(make_schedule, linear_prog_sol)
# make_schedule(4, [[4, 20, 24], [25], [7, 30, 43, 10, 16], [24, 43], [39], [37], [14, 39, 40], [
#     12, 13, 14, 38, 37], [8], [9, 5, 15, 12, 3], [40, 14], [33, 40], [7, 42, 30]], linear_prog_sol)
# Plots each function's results and a comparison of the average elapsed time, and saves the pics in json/tests/plots
# plot_test_results(3000, 'test_cases', 'corruption_strategy')
