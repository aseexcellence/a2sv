class Solution:
    '''
        making two calls to a helper function written in binary search algorithm
        will solve it efficiently. We use boolean to find both the left and
        right most element. The first time with True the second time with False
        boolean value
        '''
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.bin_search(nums, target, True)
        right = self.bin_search(nums, target, False)
        return [left, right]

    # Helper function
    def bin_search(self, nums, t, leftBias):
        l, r = 0, len(nums) - 1
        i = - 1
        while l <= r:
            m = l + (r - l) // 2
            if t > nums[m]:
                l = m + 1
            elif t < nums[m]:
                r = m - 1
            else:
                i = m
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1
        return i