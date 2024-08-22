class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(fums):
            r1 = r2 = 0
            for n in fums:
                tmp = max(n + r1, r2)
                r1 = r2
                r2 = tmp
            return r2
        return max(helper(nums[1:]), helper(nums[:len(nums) - 1])) if len(nums) > 1 else nums[0]
