import matplotlib.pyplot as plt
import random
import time

def tsp(G, start, node, visited):
    if len(visited) == len(G):
        return G[node][start]  #retornpo al inicio al finalizar
    
    costs = []
    mincost = float('inf')
    
    for edge in range(len(G)):
        if edge not in visited:
            cost = G[node][edge] + tsp(G, start, edge, visited + [edge])
            costs.append(cost)
            mincost = min(mincost, cost)

    return mincost if costs else G[node][start]

# grafo completo aleatorio con pesos en los bordes
def generate_random_complete_graph(n):
    return [[random.randint(1, 100) if i != j else 0 for j in range(n)] for i in range(n)]

# Generar 30 entradas de prueba
test_cases = [generate_random_complete_graph(n) for n in range(2, 12)] # Reducido a 10 para viabilidad

# Medir tiempos de ejecución
times = []
nodes_count = []

for i, G in enumerate(test_cases, start=2):
    start_time = time.time()
    min_cost = tsp(G, 0, 0, [0])
    end_time = time.time()
    times.append(end_time - start_time)
    nodes_count.append(i)

# Graficar los tiempos de ejecución
plt.figure(figsize=(10, 5))
plt.plot(nodes_count, times, marker='o', linestyle='-', color='b')
plt.title('Tiempos de ejecución del TSP en función del tamaño del grafo')
plt.xlabel('Número de nodos')
plt.ylabel('Tiempo de ejecución (s)')
plt.grid(True)
plt.show()
