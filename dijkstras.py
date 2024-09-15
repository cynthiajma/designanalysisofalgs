"""
Dijkstra's algorithm is used to find the shortest path from a source to destination vertex. 

Store the actual distances of each v as inf except for the source: dist[source] = 0. 

IDEA - FINDMIN: 
1. temp distance pi[v] of each vertex is calculated when we reach that edge. 
2. The temp distances are stored in a priority queue (using heap implem.) so we can quickly take the minimum distance from it
3. Heap property needs to be maintained (Bubble down)

Add this v to the visited set (S). 

IDEA - DECREASE KEY: 
1. For each neighbor of v, update the temp[v] and decrease the distance if it is shorter than the estimate. 
2. Heap property needs to be maintained (Bubble up)

"""
import heapq
class Dijkstras:
    
    def __init__(self, vertices):
        self.v = vertices 
        self.graph = [[] for _ in range(vertices)]
    
    def add_edge(self, u, v, length):
        self.graph[u].append((v, length))
        
    def dijkstra(self, source, destination):
        pq = []
        distances = [float('inf')] * self.v 
        distances[source] = 0
        
        heapq.heappush(pq, (0, source)) # use dist-values as keys in the pq
        visitedS = set() 
        while pq:
            # FIND MIN
            current_distance, u = heapq.heappop(pq) # pops v with lowest pi[v]
            if u in visitedS:
                continue 
                
            if u == destination:
                return distances[u]
            
            visitedS.add(u) 
             
            # DECREASE KEY
            for neighbor, le in self.graph[u]:
                distance = current_distance + le
                if distance < distances[neighbor]: # shorter path is found
                    distances[neighbor] = distance 
                    heapq.heappush(pq, (distance, neighbor)) 
                    # heappush automatically maintains heap property (bubble up)
                    # heappop automatically maintians heap property (bubble down)
        return distances
            
    # Example usage
if __name__ == "__main__":
    g = Dijkstras(6)
    g.add_edge(0, 1, 7)
    g.add_edge(0, 2, 9)
    g.add_edge(0, 5, 14)
    g.add_edge(1, 2, 10)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 11)
    g.add_edge(2, 5, 2)
    g.add_edge(3, 4, 6)
    g.add_edge(4, 5, 9)

    source_vertex = 0
    dest_vertex = 4
    shortest_distance = g.dijkstra(source_vertex, dest_vertex)
    # print(f"Shortest distances from vertex {source_vertex}:")
    # for i, d in enumerate(shortest_distance):
    #     print(f"Vertex {i}: {d}")
    if shortest_distance == float('inf'):
        print(f"Vertex {dest_vertex} is not reachable from vertex {source_vertex}")
    else:
        print(f"Shortest distance from vertex {source_vertex} to vertex {dest_vertex}: {shortest_distance}")