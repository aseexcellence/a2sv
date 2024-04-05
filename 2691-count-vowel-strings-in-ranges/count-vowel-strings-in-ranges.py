class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        res = []
        prefixSum = [0]
        
        for word in words:
            if word[0] in 'aeiou' and word[-1] in 'aeiou':
                prefixSum.append(prefixSum[-1] + 1)
            else:
                prefixSum.append(prefixSum[-1])
        
        for l, r in queries:
            cnt = prefixSum[r + 1] - prefixSum[l]
            res.append(cnt)
        
        return res
