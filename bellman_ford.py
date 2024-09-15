"""
The Bellman Ford Algorithm is used to find the shortest path between 2 nodes in a directed graph including negative edges. 
"""

class bellmanFord: 
    def __init__ (self, vertices):
        self.v = vertices 
        self.edges = []
    
    
    def add_edge(self, u, v, length):
        self.edges.append((u, v, length)) # storing edges and their weights
    
    
    def bellman_ford(self, source, destination):
        distances = [float('inf')] * self.v
        distances[source] = 0
        
        for i in range(self.v-1): # iterate N-1 times
            for u,v,weight in self.edges:
                if distances[u] != float('inf'): 
                    if distances[u] + weight < distances[v]:
                        distances[v] = distances[u] + weight 
       
        return distances[destination]
        
    
if __name__ == "__main__":
    g = bellmanFord(6)
    g.add_edge(0, 1, 7)
    g.add_edge(0, 2, -9)
    g.add_edge(0, 5, 14)
    g.add_edge(1, 2, 10)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 11)
    g.add_edge(2, 5, 2)
    g.add_edge(3, 4, 6)
    g.add_edge(4, 5, 9)
    
    source_vertex = 0
    dest_vertex = 4
    shortest_distance = g.bellman_ford(source_vertex, dest_vertex)
    print(shortest_distance)
    
    
    


