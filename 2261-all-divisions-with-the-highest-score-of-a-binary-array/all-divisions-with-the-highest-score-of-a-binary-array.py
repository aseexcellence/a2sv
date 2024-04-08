class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total_zeros = sum(1 for num in nums if num == 0)
        total_ones = n - total_zeros
        
        max_score = float('-inf')
        max_score_indices = []
        left_zeros = 0
        
        # Calculate the division score for each index
        for i in range(n + 1):
            right_ones = total_ones - (i - left_zeros)
            score = left_zeros + right_ones
            
            if score > max_score:
                max_score = score
                max_score_indices = [i]
            elif score == max_score:
                max_score_indices.append(i)
            
            if i < n and nums[i] == 0:
                left_zeros += 1
        
        return max_score_indices
