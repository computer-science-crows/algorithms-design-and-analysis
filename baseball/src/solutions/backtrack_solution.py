from visualiser.visualiser import Visualiser as vs


def backtrack_solution(n,m,a,s):
    
    candidates = [False for i in range(n)]
    
    answer = []

    _backtrack_solution(0,candidates,0,a,s, answer, m)

    return max(answer)

@vs(node_properties_kwargs={"shape":"record", "color":"#f57542", "style":"filled", "fillcolor":"grey"})
def _backtrack_solution(max,candidates, count, a, s, answer,m):
    
    if count == m:
        answer.append(max)
        return      

    for j in range(len(candidates)):
        if not candidates[j]:            
            candidates[j]=True
            _backtrack_solution(max + s[j][count] + a[j],candidates, count + 1, a, s, answer,m)
            candidates[j]=False

    

    



                




    

    

