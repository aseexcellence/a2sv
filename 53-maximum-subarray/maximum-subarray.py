class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxS = nums[0]
        curS = 0
        for n in nums:
            if curS < 0:
                curS = 0
            curS += n
            maxS = max(maxS, curS)
        
        return maxS