import random 
import numpy as np
from solutions import backtrack_solution


def generator(n,k,p, samples=1):

    i=0

    while i < samples:  
    
        a=[random.random() for i in range(n)]    
        s=np.random.rand(n,p+k)
        solution = backtrack_solution(n,p,k,a,s)

        

   


   
    

    

