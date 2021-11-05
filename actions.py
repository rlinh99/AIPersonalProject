from defaultData import *
import random

population = []


def mutate():
    return


def crossover():
    return


def create_default_population():
    for x in range(PROJECT_DEFAULT_POPULATION):
        sample = random.sample(range(1, 11), 10)
        if sample not in population:
            population.append(sample)


def run():
    create_default_population()
    print("I run")
    print(len(population))
