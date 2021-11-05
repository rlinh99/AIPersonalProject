from defaultData import *
import math


def calculate_distance(city1, city2):
    x = city1[0] - city2[0]
    y = city1[1] - city2[1]
    return round(math.sqrt(x ** 2 + y ** 2), 4)


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


def converges(populations):
    return True
