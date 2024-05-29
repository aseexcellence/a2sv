class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        return sum(comb(c, 2) for c in Counter(map(lambda n: n % k, accumulate([0] + nums))).values())