class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        totalSum = sum(nums)        
        for i in range(len(nums)):
            if leftSum == totalSum - leftSum - nums[i]:
                return i
            leftSum += nums[i]
        return -1
