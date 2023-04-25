from scipy.optimize import linprog
import numpy as np


def simplex_solution(n,m,a,w):
    """
    Solution of assigment problem using linear programming (simplex).
    """

    w_n = np.zeros((n,))
    w_n[:m]=w

   
    # function to minimize
    function_object = [(a[i] + a[j])- w_n[k] for i in range(n) for j in range(n) for k in range(n)]
    
    
    A_ub, b_ub = constrains(n,m)

    solution = linprog(function_object,A_ub=A_ub, b_ub=b_ub, bounds=(0,1), method='simplex')
    answer = format_answer(n, m, solution.x)

    return answer, int(-(solution.fun))


def constrains(n,m):

    b_ub =[m]
    A_ub = [[1 for i in range(n) for j in range(n) for k in range(n)]]

    return A_ub, b_ub

def format_answer(n, m, solution):
    """
    Returns solution as a list with the candidate's number as elements
    """
    answer = []
   

    for i in range(n):
        temp_1 = solution[i*n*n:(i+1)*n*n]
    
        for j in range(n):
            temp_2 = temp_1[j*n:(j+1)*n]
            for k in range(m):
                if temp_2[k] > 0:
                    answer.append((i,j,k))
         
    return answer