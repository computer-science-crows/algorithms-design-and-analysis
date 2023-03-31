from visualiser.visualiser import Visualiser as vs


def backtrack_solution(n,k,p,a,s):
    positions = [0 for i in range(p+k)]
    candidates = [False for i in range(n)]
    best_positions = [0 for i in range(p+k)]
    answer = []

    aux_backtract_solution(0,candidates,0,a,s, answer, p+k)

    return max(answer)

@vs(node_properties_kwargs={"shape":"record", "color":"#f57542", "style":"filled", "fillcolor":"grey"})
def aux_backtract_solution(max,candidates, count, a, s, answer,m):
    
    if count == m:
        answer.append(max)
        print(f'candidates  {candidates}')
        print(f'max {max}')
    
        print(f'answer {answer}')
        return
        

        #local_max = cost(positions,a,s,len(positions))  
        #print(f'local max {local_max}')      
#
        #if max < local_max:
        #    max = local_max
        #    for i in range(len(best_positions)):
        #        best_positions[i] = positions[i]
        #    return max 

         
    for j in range(len(candidates)):
        if not candidates[j]:            
            candidates[j]=True
            aux_backtract_solution(max + s[j][count], candidates, count + 1, a, s, answer,m)
            candidates[j]=False

    

    

def cost(p,a,s, count):
    sum = 0

    for i in range(count):
        sum += s[p[i],i] #+ a[p[i]]  #sumo el valor de posicion y el de moral de cada candidato

    return sum

                




    

    

