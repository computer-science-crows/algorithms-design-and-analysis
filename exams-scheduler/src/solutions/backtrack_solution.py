import numpy as np
import itertools


def backtrack_solution(k, propositions: list):

    # list with sorted propositions list
    unique_sorted_propositions= list(k for k,_ in itertools.groupby([sorted(proposition) for proposition in propositions]))    

    # print(unique_sorted_propositions)

    # boolean array to mark selected propositions
    mark = np.zeros(len(propositions), dtype=bool)

    # list of valid k propositions
    best_solution = []
    
    _backtrack_solution(unique_sorted_propositions,[], k,mark, best_solution, 0)
    
    if len(best_solution) > 0:
        return best_solution[0], True
    
    return [], False


def _backtrack_solution(propositions, current_proposition, k, mark, best_solution, count):

    # base case
    if count == k:
        if is_valid(current_proposition):
            best_solution.append(current_proposition.copy())
        return

    # in each iteration one proposition is selected
    for i in range(len(propositions)):
        if not mark[i]:
            mark[i] = True
            current_proposition.append(propositions[i])
            _backtrack_solution(propositions,current_proposition, k, mark, best_solution, count + 1)

            current_proposition.pop()
            mark[i]=False
            

def is_valid(proposition):
    '''Returns true if the intersection of the lists is empty, which means that no days match. Otherwise returns false'''
    #print(f"proposition {proposition}")
    for i in range(len(proposition)):    
        #print(f"proposition [i] {proposition [i]}")            
        for j in range(len(proposition[i])):
            for k in range(len(proposition)):
                if i != k:
                    if proposition[i][j] not in proposition[k]:
                        continue
                    else:
                        return False
            
    return True

    

    

    
