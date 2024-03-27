class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = 0
        leftc, rightc = 0, 0
        r = len(nums) - 1
        leftSum, rightSum = [0], [0]
        
        for i in range(len(nums)):
            leftSum.append(leftSum[-1] + nums[i])
            rightSum.append(rightSum[-1] + nums[-i-1])
        rightSum = rightSum[::-1]
        for i in range(len(leftSum) - 1):
            if leftSum[i] == rightSum[i + 1]:
                return i
        return - 1
            
