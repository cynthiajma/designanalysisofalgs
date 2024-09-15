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

    def find_minimum_connections(self):
        sccs = self.kosaraju()
        scc_id = [-1] * self.v
        for i, scc in enumerate(sccs):
            for node in scc: 
                scc_id[node] = i
        # build dag
        scc_count = len(sccs)
        scc_graph = [[] for _ in range(scc_count)]
        in_degree = [0] * scc_count
        scc_edges = set()
        
        for u in range(self.v):
            for v in self.graph[u]:
                # each scc_id is a NODE
                if scc_id[u] != scc_id[v] and (scc_id[u], scc_id[v]) not in scc_edges:  # different sccs
                    scc_edges.add((scc_id[u], scc_id[v]))
                    scc_graph[scc_id[u]].append(scc_id[v]) # add edges between the sccs
                    in_degree[scc_id[v]] += 1
        
        base_scc = scc_id[0] # node 0
        new_edges = 0
        for i in range(scc_count):
            if in_degree[i] == 0 and i != base_scc:
                new_edges += 1
        
        return new_edges 

if __name__ == "__main__":
    n = 6  # Number of vertices
    connections = [(0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (5, 3)] 
    k = kosarajus_algorithm(n)
    for u,v in connections:
        k.add_edge(u,v)
    result = k.find_minimum_connections()
    print(result)

    
    
    
    
                    