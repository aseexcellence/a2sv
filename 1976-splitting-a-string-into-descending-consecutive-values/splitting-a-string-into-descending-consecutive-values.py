class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(index, prev):
            if index == len(s):
                return True

            for j in range(index, len(s)):
                val = int(s[index:j + 1])
                if val + 1 == prev and backtrack(j + 1, val):
                    return True
            return False

        for i in range(len(s) - 1):
            val = int(s[:i + 1])
            if backtrack(i + 1, val):
                return True
            