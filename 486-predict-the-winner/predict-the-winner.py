class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        visited = defaultdict(int)
        def dp (l, r, t):
            if l > r:
                return 0
            if (l, r, t) in visited:
                return visited[(l, r, t)]
            res = 0
            if t == 1:
                res = max(nums[l] + dp(l + 1, r, 2), nums[r] + dp(l, r - 1, 2))
            else:
                res = min(dp(l + 1, r, 1), dp(l, r - 1, 1))
            visited[(l, r, t)] = res
            return res
        p1_score = dp(0, len(nums) - 1, 1)
        return sum(nums) - p1_score <= p1_score