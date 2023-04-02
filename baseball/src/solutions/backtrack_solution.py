import numpy as np


def backtrack_solution(n,m,a,s):
    
    # boolean array to mark selected candidates
    candidates = [False for i in range(n)]
    
    positions = [0 for i in range(m)]

    # list of best assigment of candidates and position
    best_solution = []
    
    # list of solutions
    answer = []

    _backtrack_solution(0,candidates, positions, best_solution, 0, a, s, answer)

    value = max(answer)
    solution = best_solution[answer.index(value)]  
    
    return solution.tolist(),value

def _backtrack_solution(max,candidates, positions, best_solution, count, a, s, answer):
    
    # base case
    if count == len(positions):
        answer.append(max)
        best_solution.append(np.copy(positions))        
        return      

    # in each iteration one candidate is assign to a position
    for j in range(len(candidates)):
        if not candidates[j]:            
            candidates[j]=True
            positions[count] = j
            _backtrack_solution(max + s[j][count] + a[j], candidates, positions, best_solution, count + 1, a, s, answer)
            candidates[j]=False

    

    



                




    

    

