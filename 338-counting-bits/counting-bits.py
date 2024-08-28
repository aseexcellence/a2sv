class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        If you know the number of 1s in the binary
        representation of a number i, you can easily 
        compute the number of 1s in i + 1 using previously 
        computed results. 
        The key observation is that i & (i - 1) 
        turns off the rightmost 1 in i. So, 
        countBits(i) = countBits(i & (i - 1)) + 1.
        '''
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        
        return dp