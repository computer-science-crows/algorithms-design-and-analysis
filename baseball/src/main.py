from app.generator import generator
from app.tester import tester
from solutions.backtrack_solution import backtrack_solution
from solutions.simplex_solution import simplex_solution
# from solutions.hungarian_solution_n3_attempt import hungarian_solution
from solutions.hungarian_solution import hungarian_solution
import numpy as np
import time

# generator()

# s, v = backtrack_solution(7, 6, [0, 0, 0, 0, 0, 0, 0], [[4, 10, 10, 10, 2, 9], [6, 8, 5, 12, 9, 7], [11, 9, 6, 7, 9, 5], [
#    3, 9, 6, 7, 5, 0], [2, 6, 2, 3, 2, 4], [10, 8, 11, 4, 11, 2], [3, 4, 5, 4, 3, 6]])
# print(s, v)

# print(tester(hungarian_solution))

# print(f'n: {n}')
# print(f'p: {p}')
# print(f'k: {k}')
# print(f'a: {a}')
# print(f's: {s}')
# print(f'solution: {sol}')
# print(f'values: {val}\n')

# start = time.time()
# backtrack_sol, backtrack_val = backtrack_solution(n,p+k,a,s)
# end = time.time()

# print(end-start)

# print('BACKTRACK')

# print(f'backtrack_sol {backtrack_sol}')
# print(f'bactrack_val {backtrack_val}\n')

# simplex_sol, simplex_val = simplex_solution(n, p+k, np.array(a), np.array(s))
# print(f'simplex solution: {simplex_sol}')
# print(f'simplex value: {simplex_val}')


# G = build_graph(n,p+k,a,s)
# dicc = build_dict_from_graph(G)


# print('HUNGARIAN')
# print(dicc)
# hungarian_sol = algorithm.find_matching(dicc, matching_type = 'max', return_type = 'list' )
# hungarian_val = algorithm.find_matching(dicc, matching_type = 'max', return_type = 'total')

# print(f'hungarian solution {hungarian_sol}')

# print(f'hungarian value {hungarian_val}')
