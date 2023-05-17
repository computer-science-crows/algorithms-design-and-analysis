from app.generator_relaxed import generator_relaxed
from app.tester import tester
from app.tools import plot_test_results
from solutions.backtrack_solution import backtrack_solution
from solutions.Ford_Fulkerson_solution_relaxed import corruption_strategy
from solutions.backtrack_solution_relaxed import backtrack_solution_relaxed

# Uncomment lines 11, 14 and 17 as you wish to excecute the desired functions :)

# Generates the number of test cases specified and adds them to test_cases.json
# generator_relaxed(samples=3000)

# Test solution for all tests in test_cases.json
# tester(corruption_strategy)

# Plots each function's results and a comparison of the average elapsed time, and saves the pics in json/tests/plots
# plot_test_results(3000, 'test_cases_relaxed', 'corruption_strategy')
