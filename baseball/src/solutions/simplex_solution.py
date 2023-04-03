from scipy.optimize import linprog
import numpy as np


def simplex_solution(n, m, a, s):
    """
    Solution of assigment problem using linear programming (simplex).
    """

    function_object =[]
    
    for i in range(n):
        for j in range(n):
            if j < m:
                function_object.append(-(s[i][j] + a[i]))
            else:
                function_object.append(0)


    A_eq, b_eq = constrains(n)
  
    solution = linprog(function_object, A_eq=A_eq,
                       b_eq=b_eq, bounds=None, method='simplex')
    
    answer = format_answer(n,m,solution.x)

    return answer, int(-(solution.fun))


def constrains(n):
    """
    Returns the equality constraints of the optimization problem
    """

    A_eq = []
    b_eq = [1 for i in range(2*n)]

    ones = [1 for i in range(n)]

    for i in range(n):
        temp = [0 for j in range(n*n)]
        temp[i*n:i*n + n] = ones
        A_eq.append(temp)

    for i in range(n):
        temp = [0 for j in range(n*n)]
        for j in range(n):
            temp[j*n+i] = 1
        A_eq.append(temp)

    return np.array(A_eq), np.array(b_eq)

def format_answer(n,m,solution):
    """
    Returns solution as a list with the candidate's number as elements
    """
    answer = [0 for i in range(m)]
    
    for i in range(n):
        temp = solution[i*n:i*n + n]
        for j in range(m):
            if temp[j] == 1:
                answer[j] = i

    return answer





