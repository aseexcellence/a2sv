class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def helper(i: int, j: int):
            if (j - i + 1) < 2: return (0,-1)

            hashset = set()
            for k in range(i, j + 1):
                hashset.add(s[k])
            # use parts array to store position (index) of delimeter in sorted order
            parts = [i - 1]
            for k in range(i, j + 1):
                up = s[k].upper()
                lower = s[k].lower()
                if (up not in hashset) or (lower not in hashset): # un-paired character
                    parts.append(k)
            parts.append(j+1) 
			# why do we have i - 1 and j + 1 in the array?
			# go through this example aAbbcCEdDEfF
			# the subproblems are:
			# [0, 5], [7, 8], [10, 11]
            max_len_pair = (0, -1)
			# if we don't find any delimeter, then the original string is a nice string
            if len(parts) == 2:
                return (i, j)
			# call recursively to solve each subproblem
            for i in range(len(parts) - 1):
                ni, nj = helper(parts[i] + 1, parts[i+1] - 1)
                if (nj - ni + 1) > (max_len_pair[1] - max_len_pair[0] + 1):
                    max_len_pair = (ni, nj)
            
            return max_len_pair
        
        lt, rt = helper(0, len(s) - 1)
        return s[lt:(rt+1)]