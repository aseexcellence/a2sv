class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count, d = 0, defaultdict(list)
        for i, n in enumerate(nums):
            d[n].append(i)
        for indices in d.values():
            for i, a in enumerate(indices):
                for b in indices[:i]:
                    if a*b%k == 0:
                        count += 1
        return count