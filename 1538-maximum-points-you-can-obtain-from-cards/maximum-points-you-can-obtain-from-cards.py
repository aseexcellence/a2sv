class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        f_sum, b_sum = [0], [0]
        for n in cardPoints:
            f_sum.append(f_sum[-1] + n)
        for n in cardPoints[::-1]:
            b_sum.append(b_sum[-1] + n)
        
        combined = [f_sum[i] + b_sum[k - i] for i in range(k + 1)]
        return max(combined)