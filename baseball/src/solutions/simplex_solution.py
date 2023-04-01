#from scipy.optimize import linprog

def simplex_solution(n,m,a,s):

    objective_function = [s[i][j]+ a[i] for i in range(n) for j in range(m)]
    c,b_eq = constrains(n,m)

    print(f'objective_function {objective_function}')
    print(f'c {c}')
    print(f'b_eq {b_eq}') 

    
def constrains(n,m):

    c = []
    b_eq = [1 for i in range(n*m)]

    ones = [1 for i in range(m)]

    for i in range(n):
        temp = [0 for j in range(n*m)]
        temp[i*m:i*m + m] =  ones
        c.append(temp)

    for i in range(m):
        temp = [0 for j in range(n*m)]
        for j in range(n):
            temp[j*m+i]=1
        c.append(temp)

    return c,b_eq
    

    




    
    