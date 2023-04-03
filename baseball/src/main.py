from app.generator import generator
from solutions.backtrack_solution import backtrack_solution
from solutions.simplex_solution import simplex_solution
from solutions.hungarian_solution import *
from hungarian_algorithm import algorithm
import numpy as np
import time

generator()


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
