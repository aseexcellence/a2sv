class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming_vertices = collections.defaultdict(list)
        for u, v in edges:
            incoming_vertices[v].append(u)

        unreacheable_vertices = []
        for i in range(n):
            if not incoming_vertices[i]:
                unreacheable_vertices.append(i)
        return unreacheable_vertices