import matplotlib.pyplot as plt
import random
import time
from itertools import combinations
from DaC_TSP import tsp
from DP_TSP import min_cost

def generate_random_complete_graph(n):
    return [[random.randint(1, 80) if i != j else 0 for j in range(n)] for i in range(n)]
def test_algorithms(graph_sizes):
    times_recursive = []
    times_dp = []

    for n in graph_sizes:
        G = generate_random_complete_graph(n)
        
        # Prueba del primer algoritmo (Recursivo)
        start_time = time.time()
        tsp(G, 0, 0, [0])
        end_time = time.time()
        times_recursive.append(end_time - start_time)
        
        # Prueba del segundo algoritmo (Programación Dinámica)
        start_time = time.time()
        min_cost(G)
        end_time = time.time()
        times_dp.append(end_time - start_time)

    # Gráfico de comparación
    plt.figure(figsize=(10, 5))
    plt.plot(graph_sizes, times_recursive, marker='o', linestyle='-', color='b', label='DaC')
    plt.plot(graph_sizes, times_dp, marker='o', linestyle='-', color='r', label='Programación Dinámica')
    plt.title('Comparación de tiempos de ejecución TSP')
    plt.xlabel('Número de nodos')
    plt.ylabel('Tiempo de ejecución (s)')
    plt.legend()
    plt.grid(True)
    plt.show()

graph_sizes = range(2, 12)  # Reducido para viabilidad
test_algorithms(graph_sizes)