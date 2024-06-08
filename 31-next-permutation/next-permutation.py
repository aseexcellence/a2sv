class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = k = len(nums) - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        j = i
        while j < k:
            nums[j], nums[k] = nums[k], nums[j]
            j += 1; k -= 1
        if i > 0:
            i -= 1; k = i
            while nums[k] <= nums[i]:
                k += 1
            nums[i], nums[k] = nums[k], nums[i]