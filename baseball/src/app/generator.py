import numpy as np
import os
import random
from solutions.backtrack_solution import backtrack_solution
import json
from visualiser.visualiser import Visualiser as vs

def generator(n, k, p, samples=1):

    i = 0   

    while i < samples:  
    
        a=[random.randint(0,10) for i in range(n)]    
        s= np.random.randint(low=0,high=10,size=(n,p+k))
        solution = backtrack_solution(n,p,k,a,s)
        #vs.make_animation("backtrack_solution.gif", delay=2)
        i+=1

        #save_input(n,k,p,a,s,solution)  

        return n,p,k,a,s,solution 
          


#def save_input(n,k,p,a,s,backtrack_sol):
#
#    cwd = os.getcwd()
#    cwd += "/baseball/json"
#
#
#    test_cases = {}
#
#    with open(cwd+"/test_cases.json", "r") as read_it:
#        test_cases = json.load(read_it)
#
#    with open(cwd+"/test_cases.json", "w") as write_it:
#            json.dump(t, write_it)

        




   
    

    

