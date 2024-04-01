from itertools import combinations
import matplotlib.pyplot as plt
from itertools import combinations
import random
import time

INFINITY = float('inf')

def create_index(vertex, vertex_set):
    return (vertex, frozenset(vertex_set))

def get_cost(vertex_set, prev_vertex, min_cost_dp):
    new_set = set(vertex_set)
    new_set.remove(prev_vertex)
    index = create_index(prev_vertex, new_set)
    return min_cost_dp[index]

def generate_combinations(n):
    result = []
    for r in range(n + 1):
        for subset in combinations(range(1, n + 1), r):
            result.append(set(subset))
    result.sort(key=len)
    return result

def min_cost(distance):
    min_cost_dp = {}
    parent = {}

    all_sets = generate_combinations(len(distance) - 1)

    for vertex_set in all_sets:
        for current_vertex in range(1, len(distance)):
            if current_vertex in vertex_set:
                continue
            index = create_index(current_vertex, vertex_set)
            min_cost = INFINITY
            min_prev_vertex = None

            for prev_vertex in vertex_set:
                cost = distance[prev_vertex][current_vertex] + get_cost(vertex_set, prev_vertex, min_cost_dp)
                if cost < min_cost:
                    min_cost = cost
                    min_prev_vertex = prev_vertex

            if not vertex_set:
                min_cost = distance[0][current_vertex]

            min_cost_dp[index] = min_cost
            parent[index] = min_prev_vertex

    set_of_all_vertices = set(range(1, len(distance)))
    min_cost = INFINITY
    prev_vertex = None
    for k in set_of_all_vertices:
        cost = distance[k][0] + get_cost(set_of_all_vertices, k, min_cost_dp)
        if cost < min_cost:
            min_cost = cost
            prev_vertex = k

    parent[create_index(0, set_of_all_vertices)] = prev_vertex
    # print_tour(parent, len(distance))
    return min_cost, parent 

def print_tour(parent, total_vertices):
    set_of_all_vertices = set(range(total_vertices))
    start = 0
    tour = [start]
    while True:
        set_of_all_vertices.remove(start)
        start = parent[create_index(start, set_of_all_vertices)]
        if start is None:
            break
        tour.append(start)

    print("TSP tour:")
    print("->".join(map(str, tour)))

# Generador de grafos completos con pesos aleatorios
def generate_random_complete_graph(n):
    return [[random.randint(1, 100) if i != j else 0 for j in range(n)] for i in range(n)]


# Función para probar diferentes matrices de distancia y recolectar los tiempos de ejecución
def test_and_plot(graph_sizes):
    execution_times = []
    for n in graph_sizes:
        distance_matrix = generate_random_complete_graph(n)
        start_time = time.time()
        cost, parent = min_cost(distance_matrix)
        end_time = time.time()
        execution_times.append(end_time - start_time)
        print(f"Costo mínimo para un grafo de tamaño {n}: {cost}")

    plt.plot(graph_sizes, execution_times, marker='o')
    plt.xlabel('Número de nodos')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Tiempos de ejecución de TSP usando Programación Dinámica')
    plt.grid(True)
    plt.show()

graph_sizes = range(2, 11)  # grafos de tamaño 2 a 10
test_and_plot(graph_sizes)