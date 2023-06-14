import networkx as nx
from math import inf


def BMA(G: nx.Graph):
    exclude = {}
    cost = {}
    previous = {}

    for u in G.nodes:
        exclude[f'({u},{0})']=set()
        exclude[f'({u},{0})'].add(u)
        cost[f'({u},{0})']=1
        previous[f'({u},{0})']=None

        for v in G.neighbors(u):
            exclude[f'({u},{0})'].add(v)
            cost[f'({u},{0})'] += 1
        for round in range(1,len(G.nodes)):
            previous[f'({u},{round})'] = None
            cost[f'({u},{round})'] = inf
            
    
    last_round = 0
    last_vertex = None
    
    for round in range(0,len(G.nodes)-1):
        change_cost = False
        
        for u in G.nodes:   
            try:                       
                not_adjacent_nodes = set(G.nodes).difference(set(exclude[f'({u},{round})'])) 
            except:
                continue                  
            for v in not_adjacent_nodes:
                v_exclude = set()
                v_cost = 0 
                if cost[f'({u},{round})'] < inf:
                    v_exclude.update(exclude[f'({u},{round})'])                                                       
                    v_exclude.add(v)
                    v_cost += 1 + cost[f'({u},{round})']
                
                    for j in G.neighbors(v):
                        if j not in v_exclude:
                            v_exclude.add(j)
                            v_cost += 1
                    
                    if cost[f'({v},{round + 1})'] > v_cost:
                        previous[f'({v},{round + 1})'] = u
                        exclude[f'({v},{round + 1})']= v_exclude
                        cost[f'({v},{round+1})'] = v_cost   

                        change_cost = True                 
                        last_vertex = v

                      
          
        if not change_cost:
            last_round = round                                                      
            break

    t = last_vertex
    independent_set = set()
    independent_set.add(t)

    while t != None:
        
        t = previous[f'({t},{last_round})']
        if t != None:
            independent_set.add(t)
        last_round -=1
        

    return independent_set

def bellman_ford_mis(k,p,G):

    independent_sets = list(BMA(G))
    
    if len(independent_sets) < k:
        return [], False
    
    solution = []
    for i in range(k):
        solution.append(p[independent_sets[i]])

    return solution, True





course_proposals = [
    [17, 34, 65,  87],   
    [18, 35, 66, 88],
    [18, 35, 66, 88],
    [19, 37, 67, 89],
    [20, 37, 68, 90],
    [21, 38, 69, 91],
    [22, 39, 70, 92],
    [23, 40, 71, 93],
]
k = 3

# #G = build_graph(k, course_proposals)
# G = nx.Graph([('a','c'),('a','b'),('h','a'),('h','g'),('h','f'),('g','e'),('g','d'),('e','b'),('e','f'),('d','c'),('d','f')])
# print(G.nodes)
# print(BMA(G))







    