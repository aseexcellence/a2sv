class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sq = int(sqrt(c))
        for a in range(sq + 1):
            b = sqrt(c - (a * a))
            if b == int(b): return True
        return False