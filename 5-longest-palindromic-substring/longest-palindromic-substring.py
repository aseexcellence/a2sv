class Solution:
    def longestPalindrome(self, s: str) -> str:
        def countP(l, r):
            res = ""
            resL = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resL:
                    res = s[l:r+1]
                    resL = r - l + 1
                l -= 1
                r += 1
            return (res, resL)
        
        res = []
        for i in range(len(s)):
            res.append(countP(i, i))
            res.append(countP(i, i + 1))
        
        sorted_data = sorted(res, key=lambda x: x[1], reverse=True)
        return sorted_data[0][0]