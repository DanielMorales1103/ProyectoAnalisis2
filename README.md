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
  - **Combine**: Aquí es donde se juntas las llamadas recursivas, es decir, en este algoritmo es la parte en donde se agregan a la lista de costos: `costs.append(G[node][edge]+tsp(G, start, edge, visited + [edge]))`

- Relación de recurrencia de su tiempo de ejecución:
  - Aquí notamos que hay diversas parte del algoritmo que debemos tomar en cuenta,
        tenemos $n$ problemas (nodos) en el grafo completo, y cada problema (nodo) tiene $n-1$ subconjuntos posibles de problemas (nodos), esto podría expresarse como $T(n-1)$. Además, la recurrencia está dentro de un ciclo \textbf{for}. Las demás partes del algoritmo o son $\Theta(1)$ o $\Theta(n)$ podemos concluir que la recurrencia de este algoritmo es 
$$T(n)=nT\left(n-1\right)+\Theta(n)$$

    Siendo más formalistas, tenemos 
    $$T(n)=\begin{cases}
            \Theta(1),& n=1\\
            T(n)=nT(n-1)+\Theta(n), & n>1
        \end{cases}$$
    
    Ahora, usando la técnica del árbol de recursión, tenemos: 
    
![enter image description here](https://cdn.discordapp.com/attachments/717418780065529856/1224417430303014922/663ecfa7-bb48-4381-94a6-ad495d51b84b.png?ex=661d6a97&is=660af597&hm=7ea58fb3d40e7bfcc12bfbea44076f0319860412da09e4ea2ba70e63e65520e2&)

 De esto, obtenemos: 
$$T(n)=cn+cn(n-1)+cn(n-1)(n-2)+\cdots cn!$$

Con lo que podemos concluir que el algoritmo tiene complejidad $$O(n!)$$

### Análisis empirico


## Dynamic Programming
