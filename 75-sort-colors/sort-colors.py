class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for n in nums:
            count[n] += 1
        
        t = 0
        for index, value in enumerate(count):
            for i in range(value):
                nums[t] = index
                t += 1