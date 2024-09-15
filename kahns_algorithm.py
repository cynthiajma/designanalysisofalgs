### Implement Kahn's Algorithm for topological sorting (DAG)
"""
Kahn's algorithm finds a topological ordering of a graph by repeatedly removing nodes
in the DIRECTED graph which have no incoming edges (source nodes). 

When a node is removed from a graph, it is added to the topological ordering and its edges are removed.
Then find next source node with no incoming edges and repeat. 
"""

from collections import deque 

def topological_sort(adj_list, num_nodes):
    in_degree = [0] * num_nodes # stores in-degree of each vertex 
    for i in range(num_nodes):
        for vertex in adj_list[i]:
            in_degree[vertex] += 1
    
    queue = deque() # filled with source nodes with no incoming edges + indeg = 0
    for i in range(num_nodes):
        if in_degree[i] == 0:
            queue.append(i)
            
    top_list = []
    while queue:
        source = queue.popleft()
        top_list.append(source)
        # look into adj list 
        for neighbor in adj_list[source]:
            in_degree[neighbor] += -1 
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(top_list) < num_nodes:
        print("cycle")
    return top_list
            
if __name__ == "__main__":
    num_nodes = 6
    adj_list = [[] for _ in range(num_nodes)]
    edges = [[0, 1], [1, 2], [2, 3], [4, 5], [5, 1], [5, 2]] # no cycle
    edges_cycle = [[0, 1], [1, 2], [2, 3], [4, 5], [5, 1], [5,4], [5, 2]]
    for edge in edges:
        adj_list[edge[0]].append(edge[1]) # represented like list of lists 
    result = topological_sort(adj_list, num_nodes)
    print(result)
        