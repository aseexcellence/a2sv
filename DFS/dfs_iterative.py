
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)  # Process the current node
            stack.extend(reversed(graph[vertex]))  # Add neighbors to stack in reverse order for correct processing
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

visited_nodes = dfs_iterative(graph, 'A')
print("Visited nodes:", visited_nodes)
