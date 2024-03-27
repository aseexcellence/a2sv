class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = nums
        for i in range(1, len(self.prefix)):
            self.prefix[i] += self.prefix[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right] - self.prefix[left - 1] if left > 0 else self.prefix[right]           


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)