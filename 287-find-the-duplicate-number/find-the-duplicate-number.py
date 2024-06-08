class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        p1 = 0
        for p2 in range(1, len(nums)):
            if nums[p1] == nums[p2]:
                return nums[p1]
            else:
                p1 += 1
