from actions import *
import datetime

if __name__ == '__main__':
    start = datetime.datetime.now()
    run()
    # multiple runs of GA to explore different answers
    # multiple_runs(50)
    end = datetime.datetime.now()
    time_spent = end - start
    print(f"Simulation takes: {time_spent}")

