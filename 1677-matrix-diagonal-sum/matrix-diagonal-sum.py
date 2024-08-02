class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        helper=0
        ans=0
        if len(mat) % 2 != 0:
            ans -= mat[len(mat)//2] [len(mat)//2]
        for i in mat:
            ans += i[helper] + i[-(helper+1)]
            helper += 1
        return ans