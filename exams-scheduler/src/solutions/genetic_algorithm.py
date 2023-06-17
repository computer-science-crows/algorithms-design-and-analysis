import random
import itertools


def create_initial_population(n, k):

    population = []

    ones = [1 for i in range(k)]

    for i in range(n-k+1):
        current = [0 for j in range(n)]
        current[i:i + k] = ones
        population.append(current)
    print(population)
    return population


def crossover(parent_1, parent_2, n, k):
    cross_point = random.randint(0, n)

    child_1 = parent_1.copy()
    child_2 = parent_2.copy()

    temp = child_1[0:cross_point]
    child_1[0:cross_point] = child_2[0:cross_point]
    child_2[0:cross_point] = temp

    return [child_1, child_2]


def mutate(individual, n):

    x = random.randint(0, n-1)
    y = random.randint(0, n-1)

    temp = individual[x]
    individual[x] = individual[y]
    individual[y] = temp

    return individual


def evaluate(individual, propositions, k):

    propositions_decode = []
    count = 0

    for i in range(len(individual)):
        if individual[i] > 0:
            propositions_decode.append(propositions[i])

    return len(propositions_decode) == k and len(set(propositions_decode[0]).intersection(*propositions_decode[1:])) == 0


def genetic_algorithm(k, propositions, generations=100):

    # list with sorted propositions list
    unique_sorted_propositions = list(k for k, _ in itertools.groupby(
        [sorted(proposition) for proposition in propositions]))

    n = len(unique_sorted_propositions)
    population = create_initial_population(n, k)

    for _ in range(generations):
        new_population = []
        for individual in population:
            children = crossover(list(individual), list(
                random.choice(population)), n, k)
            for child in children:
                child = mutate(child, n)
                evaluation = evaluate(child, unique_sorted_propositions, k)
                if evaluation:
                    solution = []
                    for i in range(len(child)):
                        if child[i] > 0:
                            solution.append(unique_sorted_propositions[i])
                    return solution, True
        population = new_population
    return [], False
