class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        _sum = sum(chalk)
        n = len(chalk)
        if k % _sum == 0:
            return 0
        left = k % _sum
        for i in range(n):
            left -= chalk[i]
            if left < 0:
                return i