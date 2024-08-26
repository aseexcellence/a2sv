class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        res = 1

        res *= pow(4, (n // 2), MOD)
        res *= pow(5, (n + 1) // 2, MOD)
        res %= MOD
        return res