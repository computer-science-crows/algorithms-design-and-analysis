
def backtrack_solution(n,k,p,a,s):
    positions = [0 for i in range(p+k)]
    candidates = [False for i in range(n)]
    best_positions = [0 for i in range(p+k)]

    aux_backtract_solution(0,best_positions,candidates,positions,0,a,s)

    return best_positions      


def aux_backtract_solution(max,best_positions,candidates, positions, count, a, s):
    if count == len(positions) -1:
        local_max = cost(positions,a,s,len(positions))        

        if max < local_max:
            max = local_max
            for i in range(len(best_positions)):
                best_positions[i] = positions[i] 

    else:
        
        for j in range(len(candidates)):
            if not candidates[j]:            
                candidates[j]=True
                positions[count]=j
                count +=1
                aux_backtract_solution(max,best_positions, candidates, positions, count, a, s)
                count-=1
                candidates[j]=False

def cost(p,a,s, count):
    sum = 0

    for i in range(count):
        sum += s[p[i],i] + a[p[i]]  #sumo el valor de posicion y el de moral de cada candidato

    return sum

                




    

    

