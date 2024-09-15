from kahns_algorithm import topological_sort
from collections import defaultdict

def compute_min_costs(prices, graph, n):
    top_order = topological_sort(graph, n)
    for v in top_order:
        for neighbor in graph[v]:
            prices[neighbor] = min(prices[neighbor], prices[v])
    
    return prices

if __name__ == "__main__":
    n = 6

    # Prices for nodes A, B, C, D, E, F
    prices = [5, 8, 4, 6, 3, 1]  # A = 5, B = 8, C = 4, D = 6, E = 3, F = 1

    # Graph representation as an adjacency list
    graph = defaultdict(list)
    graph[0].extend([2, 3])  # A -> C, A -> D
    graph[1].extend([3])     # B -> D
    graph[2].extend([4])     # C -> E
    graph[3].extend([5])     # D -> F

    result = compute_min_costs(prices, graph, n)
    print("Cost array:", result)
