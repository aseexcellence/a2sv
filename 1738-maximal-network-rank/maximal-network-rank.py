class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n

        for u, v in roads:
            degree[u] += 1
            degree[v] += 1

        setr = set(tuple(road) for road in roads)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                rank = degree[i] + degree[j]
                if (i, j) in setr or (j, i) in setr:
                    rank -= 1
                res = max(res, rank)
        return res

        
        
