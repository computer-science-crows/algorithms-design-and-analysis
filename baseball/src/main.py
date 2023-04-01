from app.generator import generator
from solutions.backtrack_solution import backtrack_solution
from solutions.dynamic_solution import dynamic_solution
from solutions.simplex_solution import simplex_solution
import numpy as np

n,p,k,a,s, sol= generator(6,2,1)
s_dynamic = np.negative(s)

print(f'n: {n}')
print(f'p: {p}')
print(f'k: {k}')
print(f'a: {a}')
print(f's: {s}')
print(f'solution: {sol}')

#simplex_solution(n,p+k,s,a)

dynamic_sol = dynamic_solution(n,p+k,a,s_dynamic)

print(f'dynamic solution: {dynamic_sol}')


