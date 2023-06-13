import networkx as nx
from math import inf
import itertools

def build_graph(n_c, p):

    p = list(k for k,_ in itertools.groupby([sorted(proposition) for proposition in p]))
    G = nx.Graph()

    for i in range(len(p)):
        G.add_node(i)
        prop = p[i]
        G.nodes[i]['proposition'] = prop
        G.nodes[i]['exams_number'] = len(prop)

    for i in range(len(p) - 1):
        for j in range(1, len(p)):
            intersection = set(G.nodes[i]['proposition']).intersection(
                set(G.nodes[j]['proposition']))
            if len(intersection) != 0 and i != j:
                G.add_edge(i, j)

    print('-------------G-------------')
    print('NODES')
    print(G.nodes())
    print('---------------------------')
    print('EDGES')
    print(G.edges)
    print('---------------------------')

    return G

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
            print(f"round {round}")
    
    last_round = 0
    last_vertex = None
    
    for round in range(0,len(G.nodes)-1):
        change_cost = False
        
        print(f"ROUND {round}")
        #last_round += 1
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
                        print(f"cambio costo con vertice {v} con {u} con v_costo {v_cost} < cost[f'({v},{round+1}) {cost[f'({v},{round+1})']}']")
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

    print(t)
    print(last_round)

    while t != None:
        
        t = previous[f'({t},{last_round})']
        if t != None:
            independent_set.add(t)
        last_round -=1
        

    print(f'previous {previous}')
    print(f'cost {cost}')
    print(f'exclude {exclude}')

    return independent_set


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

#G = build_graph(k, course_proposals)
G = nx.Graph([('a','c'),('a','b'),('h','a'),('h','g'),('h','f'),('g','e'),('g','d'),('e','b'),('e','f'),('d','c'),('d','f')])
print(G.nodes)
print(BMA(G))





    