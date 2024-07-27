class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i, n in enumerate(nums):
            if n == val:
                nums[i] = -1
                k += 1
        
        nums.sort(reverse=True)
        for i in range(k):
            nums.pop()
        
        