class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        pre = 0
        for a in arr:
            pre = min(pre + 1, a)
        return pre