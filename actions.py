from defaultData import *
from evaluations import *
from helpers import *
import random

population_pool = []
mating_pool = []


# mutate by in place exchange
def mutate(chromosome):
    x, y = get_mutate_points()
    temp = chromosome[x - 1]
    chromosome[x - 1] = chromosome[y - 1]
    chromosome[y - 1] = temp
    return chromosome


def crossover():
    return


# using weight average selection by rank
def select():
    selected = []
    sum_of_rank = (DEFAULT_POP_SIZE*(DEFAULT_POP_SIZE + 1)) / 2
    for i in range(0, DEFAULT_SELECTION_SIZE):
        target = random.uniform(0, 1)
        accumulated = 0
        for index, pop in enumerate(population_pool):
            rank = 30 - index
            prob = rank/sum_of_rank
            accumulated = accumulated + prob
            if accumulated > target:
                selected.append(pop)
                print(pop)
                break
    print(selected)
    print(len(selected))
    return


# create default population pool according to the size defined in defaultData.py
# insert default population
def create_default_populations():
    while len(population_pool) != DEFAULT_POP_SIZE:
        sample = random.sample(range(1, 11), 10)
        if sample not in population_pool:
            population_pool.append((sample, fitness(sample)))
    population_pool.sort(key=lambda tup: tup[1])


def run():
    create_default_populations()
    select()
    example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # result = mutate(example)
    # print(result)
    # a = fitness(example)
