"""
Kosaraju's Algorithm is used to find SCCs of an directed graph.  
1. DFS through the graph and assigns POST numbers by pushing onto STACK = LIFO
2. Transpose the graph and change direction of all edges
3. Run DFS on the transposed graph from stack order. Each DFS will give one SCC. 
"""

class kosarajus_algorithm:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [[] for _ in range(vertices)]  # Adjacency list representation of the graph
        self.transposed_graph = [[] for _ in range(vertices)]  
    
    def add_edge(self, u, v): 
        self.graph[u].append(v)
    
    # First DFS to fill the stack by POST numbers 
    def dfs1(self, v, visited, stack):
        visited[v] = True 
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs1(neighbor, visited, stack) 
        stack.append(v)  # pushed onto stack once complete
    
    # Function to transpose the graph
    def transpose(self):
        for v in range(self.v):
            for u in self.graph[v]:
                self.transposed_graph[u].append(v)  # Append to the transposed graph
    
    # DFS on the transposed graph
    def dfs2(self, vert, visited, scc):
        visited[vert] = True
        scc.append(vert) 
        for u in self.transposed_graph[vert]:
            if not visited[u]:  # Check for neighbors
                self.dfs2(u, visited, scc)
    
    def kosaraju(self):
        stack = []
        visited = [False] * self.v  # visited array for first DFS
        for i in range(self.v):
            if not visited[i]:
                self.dfs1(i, visited, stack)
        
        # Transpose the graph
        self.transpose()
        
        visited2 = [False] * self.v  # visited array for second DFS
        sccs = []
        while stack:
            vert = stack.pop()
            if not visited2[vert]:
                scc = []
                self.dfs2(vert, visited2, scc)
                sccs.append(scc)
        return sccs

# Example usage of Kosaraju's Algorithm
if __name__ == "__main__":
    g = kosarajus_algorithm(8)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(1, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(5, 3)
    g.add_edge(5, 6)
    g.add_edge(6, 7)

    sccs = g.kosaraju()
    print("Strongly Connected Components:")
    for scc in sccs:
        print(scc)
