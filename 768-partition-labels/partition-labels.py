class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = collections.defaultdict(int)
        for i, c in enumerate(s): d[c] = i
        ans, left, right = [], -1, -1
        for i, c in enumerate(s):
            right = max(right, d[c])
            if i == right:
                ans.append(right-left)
                left = i
        return ans