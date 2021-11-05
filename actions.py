from defaultData import *
from evaluations import *
from helpers import *
import random


population_pool = []
mating_poll = []

def mutate(chromosome):
    x, y = get_mutate_points()
    print("test")
    print(x)
    print(y)
    return


def crossover():
    return

# create default population pool according to the sizedefined in defaultData.py
# insert default population
def create_default_populations():
    for x in range(PROJECT_DEFAULT_POPULATION_SIZE):
        sample = random.sample(range(1, 11), 10)
        if sample not in population_pool:
            population_pool.append((sample, fitness(sample)))


def evaluate_initial_cost():
    return


def run():
    create_default_populations()
    mutate("bbb")
    a = fitness([1,2,3,4,5,6,7,8,9,10])
    print("test")
    print(a)
