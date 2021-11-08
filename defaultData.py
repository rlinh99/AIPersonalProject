"""
defaultData.py
Switch between 10 cities and 20 cities by comment out either block section.
"""
PROJECT_DEFAULT_DATA = {1: (0.3642, 0.7770),
                        2: (0.7185, 0.8312),
                        3: (0.0986, 0.5893),
                        4: (0.2954, 0.9606),
                        5: (0.5951, 0.4647),
                        6: (0.6697, 0.7657),
                        7: (0.4353, 0.1709),
                        8: (0.2131, 0.8349),
                        9: (0.3479, 0.6984),
                        10: (0.4516, 0.0488)}

# PROJECT_DEFAULT_DATA = {1: (0.3642, 0.7770),
#                         2: (0.7185, 0.8312),
#                         3: (0.0986, 0.5893),
#                         4: (0.2954, 0.9606),
#                         5: (0.5951, 0.4647),
#                         6: (0.6697, 0.7657),
#                         7: (0.4353, 0.1709),
#                         8: (0.2131, 0.8349),
#                         9: (0.3479, 0.6984),
#                         10: (0.4516, 0.0488),
#                         11: (0.2123, 0.9301),
#                         12: (0.4131, 0.1122),
#                         13: (0.1041, 0.4231),
#                         14: (0.7423, 0.9402),
#                         15: (0.3163, 0.8294),
#                         16: (0.9433, 0.0161),
#                         17: (0.5149, 0.9036),
#                         18: (0.6801, 0.7371),
#                         19: (0.6817, 0.1671),
#                         20: (0.5553, 0.6786)}

# default population size of GA
DEFAULT_POP_SIZE = 100

# default mating pool size of GA
DEFAULT_SELECTION_SIZE = 50

# default mutation rate of GA
MUTATION_RATE = 0.03

# maximum iteration of the simulation
MAX_ITERATION = 200

