class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefixSum = 0
        sumCount = {0: 1}

        for num in nums:
            prefixSum += num
            count += sumCount.get(prefixSum - k, 0)
            sumCount[prefixSum] = sumCount.get(prefixSum, 0) + 1
        return count