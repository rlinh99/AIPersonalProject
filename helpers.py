import random
from defaultData import *
from extensionData import *

def get_mutate_points():
    sample = random.sample(range(1, len(PROJECT_DEFAULT_DATA) + 1), 2)
    return sample[0], sample[1]


def find_pattern(chromosome):
    item_list = list(chromosome)
    start = 0
    end = 0
    for i, item in enumerate(EXT_PATTERN):
        index = item_list.index(item)
        if i == 0:
            start = index
        if i == len(EXT_PATTERN) -1 and EXT_PATTERN[i] in item_list:
            end = item_list.index(EXT_PATTERN[i])
            return start, end
        if item_list.index(EXT_PATTERN[i+1]) != index+1:
            return -1, -1
