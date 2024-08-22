class Solution:
    def countSubstrings(self, s: str) -> int:
        def countP(l, r):
            res = 0
            '''
            We are gonna count the palindromes using:
             1. One character at the middle and go left & right
             2. Two characters at the middle and go left & right
            The above takes care of both odd & even indexed chars in the string
            '''
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res    
        
        res = 0
        for i in range(len(s)):
            res += countP(i, i)
            res += countP(i, i + 1)
        return res
            
        