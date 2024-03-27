class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_m = 1
        r_m = 1
        n = len(nums)
        leftPro = [0] * n
        rightPro = [0] * n
        
        for i in range(n):
            j = -i - 1
            leftPro[i] = l_m
            rightPro[j] = r_m
            l_m *= nums[i]
            r_m *= nums[j]
            
        result = []
        for i in range(n):
            result.append(leftPro[i] * rightPro[i])
        
        return result