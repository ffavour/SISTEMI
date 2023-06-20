import sys


def dijkstra(graph, start):
    n = len(graph)  # Numero di nodi nel grafo

    # Inizializzazione delle distanze dei nodi come infinito tranne che per il nodo di partenza
    distances = [sys.maxsize] * n
    distances[start] = 0

    # Inizializzazione dell'insieme dei nodi visitati
    visited = [False] * n

    # Ciclo principale dell'algoritmo di Dijkstra
    for _ in range(n):
        # Trova il nodo con la distanza minima non ancora visitato
        min_distance = sys.maxsize
        min_index = -1
        for i in range(n):
            if not visited[i] and distances[i] < min_distance:
                min_distance = distances[i]
                min_index = i

        # Segna il nodo corrente come visitato
        visited[min_index] = True

        # Aggiorna le distanze dei nodi adiacenti
        for j in range(n):
            if (
                    not visited[j]
                    and graph[min_index][j] != 0
                    and distances[min_index] + graph[min_index][j] < distances[j]
            ):
                distances[j] = distances[min_index] + graph[min_index][j]

    return distances


# Matrice di adiacenza
graph = [
    [0, 2, 0, 1, 1],
    [2, 0, 2, 1, 0],
    [0, 2, 0, 3, 0],
    [1, 1, 3, 0, 1],
    [1, 0, 0, 1, 0]
]

start_node = 0  # Nodo di partenza

distances = dijkstra(graph, start_node)

# Stampa le distanze minime dai nodi di partenza a tutti gli altri nodi
print("Distanze minime:")
for i, distance in enumerate(distances):
    print(f"Nodo {i}: {distance}")
