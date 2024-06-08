class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        res = d = 0
        for i in range(len(s)):
            if s[i] == '(':
                d += 1
            else:
                d -= 1
                if s[i - 1] == '(': res += 2 ** d

        return res
