class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        evenPrefix, oddPrefix = [0] * (n + 1), [0] * (n + 1)
        
        # Compute prefix sums
        for i in range(n):
            evenPrefix[i + 1] = evenPrefix[i] + (nums[i] if i % 2 == 0 else 0)
            oddPrefix[i + 1] = oddPrefix[i] + (nums[i] if i % 2 != 0 else 0)
        
        ways = 0
        # Check each index for fair removal possibility
        for i in range(n):
            evenSum = evenPrefix[i] + (oddPrefix[n] - oddPrefix[i + 1])
            oddSum = oddPrefix[i] + (evenPrefix[n] - evenPrefix[i + 1])
            
            if evenSum == oddSum:
                ways += 1
                
        return ways
