from defaultData import *
from evaluations import *
from helpers import *
import random
import matplotlib.pyplot as plt

is_multi_run = False
final_data = []
population_pool = []
mating_pool = []
progress_pool = []
cities = []


# mutate by in place exchange
def mutate(chromosome):
    x, y = get_mutate_points()
    temp = chromosome[x - 1]
    chromosome[x - 1] = chromosome[y - 1]
    chromosome[y - 1] = temp
    return


# mutation by in place exchange, but keep the pattern
def sop_mutate(chromosome):
    head, tail = find_pattern(chromosome)
    targets = random.sample(cities, 2)
    if head != -1 and tail != -1:
        index1 = chromosome.index(targets[0])
        index2 = chromosome.index(targets[1])
        temp = chromosome[index1]
        chromosome[index1] = chromosome[index2]
        chromosome[index2] = temp
    return


def do_mutate(children, is_sop):
    for child in children:
        if is_mutation:
            if is_sop:
                sop_mutate(child)
            else:
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
    return get_offspring(gene, start, end, parent2)


def sop_crossover(parent1, parent2):
    # find pattern indexes
    p1, p2 = find_pattern(parent1)
    target = random.sample(cities, 1)[0]
    element_list = list(parent1)
    boudary_index = element_list.index(target)
    if boudary_index < p1:
        start = boudary_index
        end = p2 + 1
    elif target > p2:
        start = p1
        end = target
    else:
        start = p1
        end = p2 + 1
    gene = parent1[start:end]
    return get_offspring(gene, start, end, parent2)


# using weight average selection by rank
def select():
    while len(mating_pool) != DEFAULT_SELECTION_SIZE:
        fill_mating_pool()
        # print(len(mating_pool))
    return


def fill_mating_pool():
    sum_of_rank = (DEFAULT_POP_SIZE * (DEFAULT_POP_SIZE + 1)) / 2
    target = random.uniform(0, 1)
    accumulated = 0
    for index, pop in enumerate(population_pool):
        rank = DEFAULT_POP_SIZE - index
        prob = rank / sum_of_rank
        accumulated = accumulated + prob
        if accumulated > target and (pop[0] not in mating_pool):
            mating_pool.append(pop[0])
            break


def breed(is_sop):
    children = []
    for index, parent in enumerate(mating_pool):
        while True:
            index_parent2 = random.randint(0, len(mating_pool) - 1)
            if index != index_parent2:
                break
        if is_sop:
            child = sop_crossover(mating_pool[index], mating_pool[index_parent2])
        else:
            child = crossover(mating_pool[index], mating_pool[index_parent2])
        children.append(child)
    return children


# create default population pool according to the size defined in defaultData.py
# insert default population
def create_default_populations(is_asym):
    while len(population_pool) != DEFAULT_POP_SIZE:
        sample = random.sample(range(1, len(PROJECT_DEFAULT_DATA) + 1), len(PROJECT_DEFAULT_DATA))
        if (sample, fitness(sample)) not in population_pool:
            if is_asym:
                population_pool.append((sample, asym_fitness(sample)))
            else:
                population_pool.append((sample, fitness(sample)))


def create_seq_populations():
    global cities
    cities = list(PROJECT_DEFAULT_DATA.keys())
    for p in EXT_PATTERN:
        cities.remove(p)
    while len(population_pool) != DEFAULT_POP_SIZE:
        sample = [0] * len(PROJECT_DEFAULT_DATA)
        right_bound = len(PROJECT_DEFAULT_DATA) - len(EXT_PATTERN)
        pattern_start_index = random.randint(0, right_bound)
        for i, item in enumerate(EXT_PATTERN):
            sample[pattern_start_index + i] = item
        test = random.sample(cities, len(cities))
        for i, item in enumerate(sample):
            if item == 0:
                sample[i] = test.pop()
        population_pool.append((sample, fitness(sample)))
    # print(len(population_pool))
    return


def elite(children, is_asym):
    elite_len = len(children)
    for i in range(elite_len):
        population_pool.pop()
    for child in children:
        if is_asym:
            population_pool.append((child, asym_fitness(child)))
        else:
            population_pool.append((child, fitness(child)))
    population_pool.sort(key=lambda tup: tup[1])


def genetic_algorithm(is_asym, is_sop):
    global population_pool
    population_pool = []
    global progress_pool
    progress_pool = []
    if is_sop:
        create_seq_populations()
    else:
        create_default_populations(is_asym)

    for i in range(MAX_ITERATION):
        global mating_pool
        mating_pool = []
        select()
        children = breed(is_sop)
        do_mutate(children, is_sop)
        elite(children, is_asym)
        if population_pool[0] not in progress_pool:
            progress_pool.append(population_pool[0])
        progress_pool.sort(key=lambda tup: tup[1])
        final_data.append((i, population_pool[0][1]))
        if not is_multi_run:
            print(i, progress_pool[0])
    # return progress_pool[0]


def plot():
    x = list(map(lambda x: x[0], final_data))
    y = list(map(lambda x: x[1], final_data))
    plt.plot(x, y)
    plt.xlabel("iterations")
    plt.ylabel("cost")
    plt.show()


# main running function for the project, please comment out other
# algorithms when running the program
def run():
    # run this function for Symmetric TSP
    genetic_algorithm(False, False)

    # run this function for Asymmetric TSP
    # genetic_algorithm(True, False)

    # run this function for SOP
    # genetic_algorithm(False, True)

    plot()


def multiple_runs(count):
    global is_multi_run
    is_multi_run = True
    distinct_result_pool = []
    for i in range(0, count):
        result = genetic_algorithm(False, False)
        if result not in distinct_result_pool:
            distinct_result_pool.append(result)
        distinct_result_pool.sort(key=lambda tup: tup[1])
        print(f"The number of distinct best solutions found so far is: {len(distinct_result_pool)}")
        print(distinct_result_pool)
