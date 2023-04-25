#from app.generator import generator
#from app.tester import tester
#from app.tools import plot_test_results
from solutions.backtrack_solution import backtrack_solution
from solutions.simplex_solution import simplex_solution
#from solutions.hungarian_solution import hungarian_solution
# from solutions.hungarian_solution_n3_attempt import hungarian_solution

# Uncomment lines 12, 15, 16 and 19 as you wish to excecute the desired functions :)

# Generates the number of test cases specified and adds them to test_cases.json
# generator(samples=1)

# Test solution for all tests in test_cases.json
# tester(simplex_solution)
# tester(hungarian_solution)

# Plots each function's results and a comparison of the average elapsed time, and saves the pics in json/tests/plots
# plot_test_results()

a = [4,2,1,5]
w=[8,3,10]

sol_backtrack, val_backtrack =backtrack_solution(4,3,a,w)

print('Backtrack solution')
print(sol_backtrack)
print(val_backtrack)

sol_simplex, val_simplex = simplex_solution(4,3,a,w)

print('Simplex solution')
print(sol_simplex)
print(val_simplex)


