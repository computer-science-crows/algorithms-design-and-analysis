from app.generator import generator
from app.tester import tester
from app.tools import plot_test_results
from app.tools import comparative_plot
from solutions.backtrack_solution import backtrack_solution
from solutions.linear_prog_solution import linear_prog_sol
from solutions.genetic_algorithm import genetic_algorithm
from solutions.bellman_ford_mis import bellman_ford_mis
from solutions.make_schedule import make_schedule

# Uncomment lines 14, 17, 20-25 and 26 as you wish to excecute the desired functions :)

# Generates the number of test cases specified and adds them to test_cases.json
# generator(samples=3000)

# Test solution for all tests in test_cases.json
# tester(make_schedule, genetic_algorithm)

# Plots each function's results and a comparison of the average elapsed time, and saves the pics in json/tests/plots
# plot_test_results(3000, 'test_cases', 'linear_prog_sol',
#                   'Programación Lineal', 'lightgreen')
# plot_test_results(3000, 'test_cases', 'genetic_algorithm',
#                   'Algoritmo Genético', 'plum')
# plot_test_results(3000, 'test_cases', 'bellman_ford_mis',
#                   'BMA', 'skyblue')
# comparative_plot(3000, 'test_cases')
