'''
procedure BFS(G, root) is:
    let Q be a queue
    label root as explored
    Q.enqueue(root)
    while Q is not empty do:
        v := Q.dequeue()
        if v is the goal then:
            return v
        for all edges from v to w in G.adjacentEdges(v) do:
            if w is not labeled as explored then:
                label w as explored
                w.parent := v
                Q.enqueue(w)
'''
'''
Time Complexity: O(|V| + |E|) = O(b^d) -> we visit a node once, 
and if it's a complete graph we will also use every edge
Space Complexity: O(|V|) = O(b^d) -> the space required to input
the nodes in the visited set
Optimal for unweighted graphs
When working infinite graphs its more practical to describe the
complexity of bfs in terms: to find the nodes that are at distance
d from the start node, BFS takes O(b^(d + 1)) time and memory, where
b is the "branching factor" of the graph.
'''
'''
BFS is complete, but DFS is not. When applied to infinite graphs
represented implicitly--in the application of graph traversal
methods in AI--BFS will eventually find the goal state, but DFS
may get lost in parts of the graph that have no goal state and
never return.
'''
from collections import deque

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, u, v):
        if u not in self.edges:
            self.edges[u] = []
        self.edges[u].append(v)
        # Assuming undirected graph, add the opposite edge as well
        if v not in self.edges:
            self.edges[v] = []
        self.edges[v].append(u)

    def adjacent_edges(self, v):
        return self.edges[v] if v in self.edges else []

class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None

def bfs(graph, root, goal):
    Q = deque()
    explored = set()

    Q.append(root)
    explored.add(root)

    while Q:
        v = Q.popleft()
        if v.value == goal.value:
            return v
        for w in graph.adjacent_edges(v.value):
            if w not in explored:
                explored.add(w)
                w.parent = v
                Q.append(w)

    return None

    '''
    Implementation with Stack
    # q = []
    # visited = set()
    # parent = {}

    # q.append(root)
    # visited.add(root)

    # while q:
    #     v = q.pop(0)
    #     if v == goal:
    #         return v, parent
        
    #     for w in graph.adjacent_edges(v):
    #         if w not in visited:
    #             visited.add(w)
    #             parent[w] = v
    #             q.append(w)

    # return None, parent
    '''

# Example usage:
# Create nodes
nodes = {i: Node(i) for i in range(5)}

# Create a graph and add edges
g = Graph()
g.add_edge(nodes[0], nodes[1])
g.add_edge(nodes[0], nodes[2])
g.add_edge(nodes[1], nodes[3])
g.add_edge(nodes[2], nodes[3])
g.add_edge(nodes[3], nodes[4])

# Run BFS
root = nodes[0]
goal = nodes[0]
result = bfs(g, root, goal)

# Trace the path if the goal is found
if result:
    path = []
    while result:
        path.append(result.value)
        result = result.parent
    path.reverse()
    print("Path to goal:", path)
else:
    print("Goal not found.")



