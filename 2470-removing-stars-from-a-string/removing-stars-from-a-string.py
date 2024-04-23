class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        for char in s:
            if char == "*":
                res and res.pop()
            else:
                res.append(char)
        return "".join(res)
        
            