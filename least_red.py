"""
    This algorithm determines the following for an undirected acyclic graph: 
    1. Is G bipartite?
    2. Returns a least-red coloring (List of bool where True = red, False = blue)
    
    Note: undirected graph has connected components. 
"""
from collections import deque 


def build_adj_list(n, edges):
    graph = [[] for _ in range(n)]
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph


"""
dfs here checks for a valid coloring. If there is no valid coloring, then it returns False. 
"""
def dfs(vertex: int, current_color: bool, color, graph, count, component) -> bool: 
    color[vertex] = current_color # assign color to current 
    component.append(vertex)
    if current_color:
        count[0] += 1
    else:
        count[1] += 1
    for neighbor in graph[vertex]:
        if color[neighbor] is None: 
            if not dfs(neighbor, not current_color, color, graph, count, component): # opposite coloring returns False?
                return False 
        elif color[neighbor] == current_color:
            return False # there is a conflict
    return True
        

def least_red(n:int, edges:list[(int, int)]) -> list[bool]:
    graph_adjlist = build_adj_list(n, edges)
    color = [None] * n
    # perform dfs to color the graph: 
    for i in range(n):
        if color[i] is None: # new component
            count = [0,0]
            component = []
            if not dfs(i, False, color, graph_adjlist, count, component): # meaning that there is no valid coloring
                return None 
        if count[0] > count[1]: # only flip the color in the component
                for node in component:
                    color[node] = not color[node]
    
    return color

# if __name__ == "__main__":
#     # # not BP
#     # n = 5
#     # edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
#     # coloring = least_red(n, edges)
#     # print(coloring)
    
#     #BP
#     n = 6
#     edges = [(0, 1), (0, 2), (3,5), (4,5)]
#     coloring = least_red(n, edges)
#     print(coloring)



    