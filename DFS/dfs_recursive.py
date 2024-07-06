'''
 Recursive DFS IMplementation
'''
 
def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    # print(start)  # Process the current node
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    return visited

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited_nodes = dfs_recursive(graph, 'A')
print("Visited nodes:", visited_nodes)
