from app.generator import generator
from app.tester import tester
from app.tools import plot_test_results
from solutions.backtrack_solution import backtrack_solution
from solutions.Ford_Fulkerson_solution import max_flow_min_cut


# Uncomment lines 12, 15, 16 and 19 as you wish to excecute the desired functions :)

# Generates the number of test cases specified and adds them to test_cases.json
generator(samples=4000)

# Test solution for all tests in test_cases.json
# tester(simplex_solution)
# tester(hungarian_solution)

# Plots each function's results and a comparison of the average elapsed time, and saves the pics in json/tests/plots
# plot_test_results()


sol, val = backtrack_solution(4, 5, [1, 5, 2, 2], [4, 4, 5, 2, 2])

print(f"solucion backtrack {sol}")
print(f'valor backtrack {val}')
