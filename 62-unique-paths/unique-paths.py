class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for i in range(m - 1):
            newR = [1] * n
            for j in range(n - 2, -1, -1):
                newR[j] = newR[j + 1] + row[j]
            row = newR
        return row[0]