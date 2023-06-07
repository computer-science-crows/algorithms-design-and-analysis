import numpy as np


def backtrack_solution(k, exams, propositions: list):

    # list with sorted propositions list
    sorted_propositions = [proposition.sort() for proposition in propositions]

    # boolean array to mark selected propositions
    mark = np.zeros(len(propositions), dtype=bool)

    # list of valid k propositions
    best_solution = []

    _backtrack_solution(propositions,[], k, best_solution, 0)


    # list of propositions with the appropriate size
    solution = k_valid_propositions(exams, best_solution)

    return solution




def _backtrack_solution(propositions, current_proposition, k, mark, best_solution, count):

    # base case
    if count == k:
        if is_valid(current_proposition):
            best_solution.append(current_proposition)
        return

    # in each iteration one proposition is selected
    for i in range(len(propositions)):
        if not mark[i]:
            mark[i] = True
            current_proposition.append()
            _backtrack_solution(propositions, k, mark, best_solution, count + 1)
            mark[i]=False
            


def is_valid(proposition):
    '''Returns true if the intersection of the lists is empty, which means that no days match. Otherwise returns false'''

    intersection = set(proposition[0]).intersection(*proposition[1:])

    return len(intersection) == 0


def k_valid_propositions(exams, propositions):
    '''Returns the proposed list that matches the number of exams per course. Otherwise, it returns the empty set.'''

    sorted_exams = exams.sort()
    valid = True
    
    for proposition in propositions:
        sorted_proposition = sorted(proposition, key=len)
        for i in range(len(exams)):
            if exams[i] != len(sorted_proposition[i]):
                valid = False
                break
        if valid:
            return proposition
        

    return []

    




    

    

    
