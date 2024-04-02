
## *Travelling Salesman Problem* (TSP):
"Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?"

## Divide and Conquer

### Análisis teórico
 Considérese el $\textit{Travelling Salesman Problem} (TSP):$
```python
def tsp(G, start, node, visited):
    costs = []
    nextone = -1
    minactual = 10000000
    for edge in range(len(G[node])):
        if (edge not in visited):
            costs.append(G[node][edge]+tsp(G, start, edge, visited + [edge]))
            mintemporal = min(costs)
            if (minactual >= mintemporal):
                nextone = edge
                minactual = mintemporal
        if (len(costs)>0):
            visited.append(nextone)
            return min(costs)
        else:
            return G[node][start]
```

Entonces,

- Divide-Conquer-Combine:
  - **Divide**: Es la parte en el que el problema se divide en subproblemas. En este caso tenemos al **for** que itera a cada **edge** y el condicional `if (edge not in visited)` el cual subdivide el problema a los *edges* no visitados.
  - **Conquer**: En esta parte es donde se ejecutan las llamadas recursivas. En este caso particular es cuando se ejecuta `tsp(G, start, edge, visited + [edge])`
  - **Combine**: Aquí es donde se juntan las llamadas recursivas, es decir, en este algoritmo es la parte en donde se agregan a la lista de costos: `costs.append(G[node][edge]+tsp(G, start, edge, visited + [edge]))`

- Relación de recurrencia de su tiempo de ejecución:
  - Aquí notamos que hay diversas parte del algoritmo que debemos tomar en cuenta,
        tenemos $n$ problemas (nodos) en el grafo completo, y cada problema (nodo) tiene $n-1$ subconjuntos posibles de problemas (nodos), esto podría expresarse como $T(n-1)$. Además, la recurrencia está dentro de un ciclo $\textbf{for}$. Las demás partes del algoritmo o son $\Theta(1)$ o $\Theta(n)$ podemos concluir que la recurrencia de este algoritmo es 
$$T(n)=nT\left(n-1\right)+\Theta(n)$$

    Siendo más formalistas, tenemos

```math
 $$T(n)=\begin{cases}
            \Theta(1),& n=1\\
            T(n)=nT(n-1)+\Theta(n), & n>1
        \end{cases}$$

```    

Ahora, usando la técnica del árbol de recursión, tenemos: 
    
![enter image description here](https://cdn.discordapp.com/attachments/717418780065529856/1224417430303014922/663ecfa7-bb48-4381-94a6-ad495d51b84b.png?ex=661d6a97&is=660af597&hm=7ea58fb3d40e7bfcc12bfbea44076f0319860412da09e4ea2ba70e63e65520e2&)

 De esto, obtenemos: 
$$T(n)=cn+cn(n-1)+cn(n-1)(n-2)+\cdots cn!$$

Con lo que podemos concluir que el algoritmo tiene complejidad $$O(n!)$$

### Análisis empirico

Como entrada en ambas pruebas, se utilizaron grafos completos aleatorios con pesos en los bordes: 

```python
def generate_random_complete_graph(n):
    return [[random.randint(1, 100) if i != j else 0 for j in range(n)] for i in range(n)]
```

Gráfica
![enter image description here](https://cdn.discordapp.com/attachments/717418780065529856/1224518856546975774/WhatsApp_Image_2024-04-01_at_18.29.29.jpeg?ex=661dc90d&is=660b540d&hm=c3cf9d94f225bf4db8a3de489e76ef11d957f27df13cb4a29041638bc9ab6c0d&)

## Dynamic Programming
### Análisis teórico

Considérese la siguiente matriz de distancias

||0 |1|2|3
|--|--|--|--|--|
| 0 | 0 |1|15|6
| 1 | 2 |0|7|3
| 2 | 9 |6|0|12
| 3 | 10 |4|8|0

**Iniciando desde vertex 0**

Posibles subsets: 

	 - 0
	 - {1}, {2}, {3}
	 - {1,2}, {2,3}, {1,3}
	 - {1,2,3}

**Cálculo de costos:** 

|  |  Cost|Parent
|--|--|--|
| [1,0] |1  |0
| [2,0] |15  |0
| [3,0] |6  |0
| [2,{1}] |1+7 = 8  |1
| [3,{1}] |1+3 = 4  |1
| [1,{2}] |15+6 = 21  |2
| [3,{2}] |15+12 = 27  |2
| [1,{3}] |6+4 = 10  |3
| [2,{3}] |6+8 = 14  |3
| [3,{1,2}] |min[3+21, 12+8] = 20  |2
| [3,{1,2}] |min[3+21, 12+8] = 20  |2
| [1,{2,3}] |min[6+14, 4+27] = 20  |2
| [2,{1,3}] |min[7+10, 8+4] = 12  |3
| [0,{1,2,3}] |min[2+20, 9+12, 10+20] = 21  |2


**Tour:** 
0 -> 2 -> 3 -> 1 -> 0

**Entonces:** 

$$T(n)=O(2^{n} n^{2})$$

Donde 
$$2^{n} $$ es el número exponencial de subsets
Y 
$$n^{2}$$ se debe a verificar cuál debería de ser el vértice anterior del vértice actual

### Análisis empirico
Gráfica
![enter image description here](https://cdn.discordapp.com/attachments/717418780065529856/1224519099736920165/WhatsApp_Image_2024-04-01_at_18.29.42.jpeg?ex=661dc947&is=660b5447&hm=665300f50aeb6ab2af336158813e298d8a43349ff0a35cc31c06d0a71920c86e&)

## Comparación y conclusiones

![enter image description here](https://cdn.discordapp.com/attachments/717418780065529856/1224519303517179934/WhatsApp_Image_2024-04-01_at_18.30.39.jpeg?ex=661dc978&is=660b5478&hm=cbe4bf75104de878a02e400cfed7647beb0740faf788417ca11248e185a1342a&)

Los tiempos de ejecución empíricos obtenidos a partir de la ejecución del algoritmo son consistentes con la complejidad factorial $$O(n!)$$ que descrito en el análisis teórico. Específicamente, observamos que el tiempo de ejecución se mantiene bastante manejable para grafos pequeños, pero aumenta de manera explosiva a medida que el número de nodos crece. 

En el caso ideal teórico, la relación de recurrencia $$T(n)=nT\left(n-1\right)+\Theta(n)$$
 sugiere que cada incremento en el número de nodos multiplica el tiempo de ejecución por aproximadamente el número de nodos, lo cual se manifestaría como una curva que crece extremadamente rápido. En la práctica, vemos este comportamiento con el rápido aumento de los tiempos de ejecución al aumentar el número de nodos, indicando que los tiempos empíricos están en buena alineación con las expectativas teóricas.

Sin embargo,  discrepancias o diferencias entre el análisis teórico y la evidencia empírica podrían surgir por varias razones:

1.  **Optimizaciones del Intérprete/Compilador:** El intérprete de Python o el sistema en el que se ejecuta el código puede tener optimizaciones que afecten el tiempo de ejecución real.
    
3.  **Variabilidad en los Datos de Entrada:** La complejidad factorial asume el peor caso en términos de la secuencia de nodos visitados. En la realidad, algunos caminos pueden tener una longitud significativamente más corta que otros debido a la aleatoriedad en los pesos de los bordes, lo que podría hacer que algunas instancias sean resueltas más rápidamente que otras.

También es interesante darse cuenta que el algoritmo de DaC tiene el tiempo de ejecución resultante al utilizar el approach de Brute Force. Esto puede deberse a que este problema es computacionalmente complejo, incluso, que este es un NP-Problem, por lo que no se ha encontrado ninguna solución eficiente al problema. Y realmente en el algoritmo DaC estamos aplicacando una solución recursiva, por lo que su tiempo de ejecución se ve afectado en gran medida. 

Por otro lado, el acercamiento de Dynnamic Programming utiliza un enfoque de **Bottom-Up**. El código genera todas las combinaciones posibles de subconjuntos de vértices y luego procede a calcular el costo mínimo de viaje que incluye esos subconjuntos, partiendo de los casos base más pequeños hacia soluciones más completas. Es decir, se comienza desde los casos más simples y se avanza hacia el problema completo. 

Este último enfoque bottom-up es eficiente para este problema ya que asegura que todos los subproblemas necesarios se han resuelto antes de intentar calcular la solución a un problema más grande. Además, al evitar la recursividad, se reducen los costos de llamadas a funciones y se maneja mejor el uso de memoria, lo cual es especialmente relevante en problemas de optimización combinatoria como el TSP, donde el número de subproblemas puede crecer exponencialmente con el tamaño del problema. Y esto se puede notar en las gráficas de comparación. 

También valdría la pena explorar un algoritmo greedy, ya que su tiempo de ejecución es polinómico,
$$T(n)=O(n^{2} log_{n})$$

Sin embargo debemos de considerar la falta de optimalidad, ya que no hay garantía de que se encuentre la solución óptima global. Los algoritmos greedy toman decisiones óptimas locales con la esperanza de que estas decisiones conduzcan a una solución óptima global, lo cual no siempre es el caso.
