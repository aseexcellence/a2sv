class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        res = [[] for _ in range(n)]
        graph = [[] for _ in range(n)]

        def dfs(parent, curr, visit):
            visit[curr] = True
            for dest in graph[curr]:
                if not visit[dest]:
                    res[dest].append(parent)
                    dfs(parent, dest, visit)

        for edge in edges:
            graph[edge[0]].append(edge[1])
        
        for i in range(n):
            dfs(i, i, [False] * n)
        
        for i in range(n):
            res[i].sort()

        return res
        