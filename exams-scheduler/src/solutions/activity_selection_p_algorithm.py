
def activity_selection_solution(k, propositions):

    # list with sorted propositions list
    sorted_propositions = [sorted(proposition) for proposition in propositions]

    propositions_w_intervals = build_intervals(sorted_propositions)
    
    activities = [(start_day, end_day) for proposal in propositions_w_intervals for (start_day, end_day) in proposal]

    activities.sort(key=lambda x: x[1])

    selected_proposals = []

    for activity in activities:
        if all(activity not in proposal for proposal in selected_proposals):
            selected_proposals.append([proposal.copy() for proposal in propositions_w_intervals if activity[1] in [day for (day, _) in proposal]][0])
            if len(selected_proposals) == k:
                break
   
    return remove_intervals()


def build_intervals(propositions):
    '''Converts the list of propositions to a list with each proposition as 
    a three-tuple of the following form (smallest day, largest day, size of proposal)'''

    propositions_w_intervals = []

    for proposition in propositions:
        proposition_w_interval = []
        for day in proposition:
            proposition_w_interval.append((day,day))
        propositions_w_intervals.append(proposition_w_interval)            

    return propositions_w_intervals

def remove_intervals(selected_propositions):

    propositions = []

    for proposition in selected_propositions: 
        current_proposition = []       
        for (i,j) in proposition:
           current_proposition.append(i)
        propositions.append(current_proposition)            

    return propositions

course_proposals = [
    [17, 34, 65,  87],
    [17, 34, 65, 87],
    [17, 34, 65, 87],
    [18, 35, 66, 88],
    [18, 35, 66, 88],
    [19, 36, 67, 89],
    [20, 37, 68, 90],
    [21, 38, 69, 91],
    [22, 39, 70, 92],
    [23, 40, 71, 93],
]
k = 3

print(activity_selection_solution(k,course_proposals))