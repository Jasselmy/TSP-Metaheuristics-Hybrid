import time
import pandas as pd
from reader import read_instance
from greedy import nearest_neighbor
from threshold_accepting import threshold_accepting
from simulated_annealing import simulated_annealing
from hybrid_metaheuristic import hybrid_solver
from tsp_utils import tour_length

def run_experiment(instance_file):
    D = read_instance(instance_file)
    results = []

    start = time.time()
    s = nearest_neighbor(D)
    results.append(["Greedy", tour_length(s,D), round(time.time()-start,3)])

    start = time.time()
    s = threshold_accepting(D, s)
    results.append(["Threshold Accepting", tour_length(s,D), round(time.time()-start,3)])

    start = time.time()
    s = simulated_annealing(D, s)
    results.append(["Simulated Annealing", tour_length(s,D), round(time.time()-start,3)])

    start = time.time()
    s = hybrid_solver(D)
    results.append(["Hybrid", tour_length(s,D), round(time.time()-start,3)])

    df = pd.DataFrame(results, columns=["Méthode", "Distance", "Temps (s)"])
    return df

if __name__ == "__main__":
    for instance in ["data/instance_29.txt", "data/instance_51.txt"]:
        print(f"\nRésultats pour {instance} :")
        df = run_experiment(instance)
        print(df)
