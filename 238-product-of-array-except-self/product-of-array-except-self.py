class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        leftPro, rightPro = 1, 1
        
        for i in range(len(nums)):
            result[i] *= leftPro
            leftPro *= nums[i]
            result[len(nums) - 1 -i] *= rightPro
            rightPro *= nums[len(nums) - 1 - i]
            
        return result