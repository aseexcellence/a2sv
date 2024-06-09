class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
      m, n = len(mat), len(mat[0])
      ans = [[0 for _ in range(n)] for _ in range(m)]
      
      for i in range(m):
        rowStart, rowEnd = max(0, i-k), min(m, i+k+1)
        for j in range(n):
          colStart, colEnd = max(0, j-k), min(n, j+k+1)
          for l in range(rowStart, rowEnd):
            ans[i][j] += sum(mat[l][colStart:colEnd])
      
      return ans