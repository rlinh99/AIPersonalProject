from defaultData import *
from extensionData import *
import math
import random


def calculate_distance(city1, city2):
    x = city1[0] - city2[0]
    y = city1[1] - city2[1]
    return math.sqrt(x ** 2 + y ** 2)


def calculate_asym_distance(city1, city2):
    x = city1[0] - city2[0]
    y = city1[1] - city2[1]


def fitness(route):
    score = 0
    for index, city_num in enumerate(route):
        next_index = index + 1
        if next_index == len(PROJECT_DEFAULT_DATA):
            next_index = 0
        next_city = route[next_index]
        score = score + calculate_distance(PROJECT_DEFAULT_DATA[city_num]
                                           , PROJECT_DEFAULT_DATA[next_city])
    return score


def asym_fitness(route):
    score = 0
    for index, city_num in enumerate(route):
        next_index = index + 1
        if next_index == len(PROJECT_DEFAULT_DATA):
            next_index = 0
        next_city = route[next_index]
        if city_num < next_city:
            score = score + calculate_distance(PROJECT_DEFAULT_DATA[city_num],
                                               PROJECT_DEFAULT_DATA[next_city])
        else:
            score = score + calculate_distance(EXTENSION_ASYM_DATA[city_num],
                                               EXTENSION_ASYM_DATA[next_city])
    return score


# crossover uses order based representation
def get_offspring(gene, start, end, parent):
    parent_copy = list(parent)
    orig_length = len(parent_copy)
    result = [0] * orig_length
    for index, item in enumerate(gene):
        parent_copy.remove(item)
        result[start + index] = item
    for index2, item2 in enumerate(parent_copy):
        filling_index = end + index2
        if filling_index >= orig_length:
            filling_index = filling_index - orig_length
        result[filling_index] = item2
    return result


def is_mutation():
    rand = random.uniform(0, 1)
    if rand < MUTATION_RATE:
        return True
    return False
