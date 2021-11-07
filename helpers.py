import random
from defaultData import *

def get_mutate_points():
    sample = random.sample(range(1, len(PROJECT_DEFAULT_DATA)+1), 2)
    return sample[0], sample[1]