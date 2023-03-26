import numpy as np
#import sys
#sys.path.append('..')
from solutions.backtrack_solution import backtrack_solution


def generator(n, k, p, samples=1):

    i = 0

    while i < samples:  
    
        a=[random.randint(0,10) for i in range(n)]    
        s= np.random.randint(low=0,high=10,size=(n,p+k))
        solution = backtrack_solution(n,p,k,a,s)
        i+=1
        

        return n,k,p,a,s, solution

        




   
    

    

