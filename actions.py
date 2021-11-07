from defaultData import *
from evaluations import *
from helpers import *
import random
import matplotlib.pyplot as plt


final_data = []
population_pool = []
mating_pool = []
progress_pool = []


# mutate by in place exchange
def mutate(chromosome):
    x, y = get_mutate_points()
    temp = chromosome[x - 1]
    chromosome[x - 1] = chromosome[y - 1]
    chromosome[y - 1] = temp
    return


def do_mutate(children):
    for child in children:
        if is_mutation:
            mutate(child)
    return


def crossover(parent1, parent2):
    # cross point
    cp = random.randint(0, 9)
    while True:
        cp2 = random.randint(0, 9)
        if cp2 != cp:
            break
    if cp < cp2:
        start = cp
        end = cp2
    else:
        start = cp2
        end = cp
    gene = parent1[start:end]
    return get_offstring(gene, start, end, parent2)


# using weight average selection by rank
def select():
    sum_of_rank = (DEFAULT_POP_SIZE * (DEFAULT_POP_SIZE + 1)) / 2
    for i in range(0, DEFAULT_SELECTION_SIZE):
        target = random.uniform(0, 1)
        accumulated = 0
        for index, pop in enumerate(population_pool):
            rank = DEFAULT_POP_SIZE - index
            prob = rank / sum_of_rank
            accumulated = accumulated + prob
            if accumulated > target:
                mating_pool.append(pop[0])
                break
    return


def breed():
    children = []
    for index, parent in enumerate(mating_pool):
        while True:
            index_parent2 = random.randint(0, len(mating_pool) - 1)
            if index != index_parent2:
                break
        child = crossover(mating_pool[index], mating_pool[index_parent2])
        children.append(child)
    return children


# create default population pool according to the size defined in defaultData.py
# insert default population
def create_default_populations():
    while len(population_pool) != DEFAULT_POP_SIZE:
        sample = random.sample(range(1, 11), 10)
        if (sample, fitness(sample)) not in population_pool:
            population_pool.append((sample, fitness(sample)))


def elite(children):
    elite_len = len(children)
    for i in range(elite_len):
        population_pool.pop()
    for child in children:
        population_pool.append((child, fitness(child)))
    population_pool.sort(key=lambda tup: tup[1])


def genetic_algorithm():
    create_default_populations()
    for i in range(MAX_ITERATION):
        global mating_pool
        mating_pool = []
        select()
        children = breed()
        do_mutate(children)
        elite(children)
        if population_pool[0] not in progress_pool:
            progress_pool.append(population_pool[0])
        progress_pool.sort(key=lambda tup: tup[1])
        print(progress_pool)
        final_data.append((i, population_pool[0][1]))

    return


def asym_genetic_algorithm():
    return


def run():
    genetic_algorithm()
    x = list(map(lambda x: x[0], final_data))
    y = list(map(lambda x: x[1], final_data))
    plt.plot(x,y)
    plt.xlabel = "iterations"
    plt.ylabel = "cost"
    plt.show()
    # asym_genetic_algorithm()
    #([6, 2, 9, 1, 4, 8, 3, 7, 10, 5], 2.5832228012801766)
    # a = [6, 2, 9, 1, 4, 8, 3, 7, 10, 5]
    # q = fitness(a)
    # print(q)
