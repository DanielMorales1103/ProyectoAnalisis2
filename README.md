## *Travelling Salesman Problem* (TSP):

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
