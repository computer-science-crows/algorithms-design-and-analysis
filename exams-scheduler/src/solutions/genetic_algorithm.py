import random
import itertools


def create_initial_population(n, k):

    base = [1 if i < k else 0 for i in range(n)]
    population = list(set(itertools.permutations(base)))

    return population[0:k]   



def crossover(parent_1, parent_2, n, k):
    cross_point = random.randint(0,n)

    child_1 = parent_1.copy()
    child_2 = parent_2.copy()


    temp = child_1[0:cross_point]
    child_1[0:cross_point] = child_2[0:cross_point]
    child_2[0:cross_point] = temp

    return [child_1,child_2]


def mutate(individual,n):
    
    x = random.randint(0,n-1)
    y= random.randint(0,n-1)

    temp = individual[x]
    individual[x]=individual[y]
    individual[y]=temp

    return individual


def evaluate(individual, propositions, k):

    propositions_decode = []
    count = 0

    for i in range(len(individual)):
        if individual[i] > 0:
            propositions_decode.append(propositions[i])              
                
                   
    return len(propositions_decode) == k and len(set(propositions_decode[0]).intersection(*propositions_decode[1:])) == 0


def genetic_algorithm(k, propositions, generations):

    # list with sorted propositions list
    unique_sorted_propositions= list(k for k,_ in itertools.groupby([sorted(proposition) for proposition in propositions]))

    n=len(unique_sorted_propositions)
    population = create_initial_population(n, k)

    for _ in range(generations):
        new_population = []
        for individual in population:
            children = crossover(list(individual), list(random.choice(population)),n,k)           
            for child in children:
                child = mutate(child,n)
                evaluation = evaluate(child, unique_sorted_propositions,k)
                if evaluation:
                    solution = []
                    for i in range(len(child)):
                        if child[i] > 0:
                            solution.append(unique_sorted_propositions[i])
                    return solution
        population = new_population  
    return []


course_proposals = [
    [17, 34, 65,  87],   
    [18, 35, 66, 88],
    [18, 35, 66, 88],
    [19, 36, 67, 89],
    [20, 37, 68, 90],
    [21, 38, 69, 91],
    [22, 39, 70, 92],
    [23, 40, 71, 93],
]
k = 3

print(genetic_algorithm(k,course_proposals,100))