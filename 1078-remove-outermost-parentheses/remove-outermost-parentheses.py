class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        cc = bc = split = 0
        res = ""
        for i in range(len(s)):
            if s[i] == '(':
                cc += 1
            else:
                bc += 1
            if bc == cc:
                res += s[split+1 : i]
                split = i + 1
                bc = cc = 0
        
        return res
        
