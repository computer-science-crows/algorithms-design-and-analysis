import numpy as np
import itertools


def backtrack_solution(k, propositions: list):

    # list with sorted propositions list
    unique_sorted_propositions= list(k for k,_ in itertools.groupby([sorted(proposition) for proposition in propositions]))    

    print(unique_sorted_propositions)

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

    intersection = set(proposition[0]).intersection(*proposition[1:])

    return len(intersection) == 0



course_proposals = [
   [[56, 45, 43, 14, 1], [5, 58, 28, 43, 20]]
]
k = 2

print(backtrack_solution(k,course_proposals))

    




    

    

    
