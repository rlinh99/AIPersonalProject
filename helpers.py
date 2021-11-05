import random


def get_mutate_points():
    sample = random.sample(range(1, 11), 2)
    return sample[0], sample[1]