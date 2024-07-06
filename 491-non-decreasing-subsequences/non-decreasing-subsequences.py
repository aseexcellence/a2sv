class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        """
        Let's try our best. The conditions are:
        1. pick the next num IFF its equal or greater than prev num
        2. Or we do not pick that element and increase the index 
        3. if a subsequence of atleast two elements is found its valid result
        """

        stack = []
        res = set()

        def backtrack(idx):
            if idx >= len(nums):
                if len(stack) > 1:
                    res.add(tuple(stack))
                return
            
            if not stack or nums[idx] >= stack[-1]:
                stack.append(nums[idx])
                backtrack(idx + 1)
                stack.pop()

            backtrack(idx + 1)

        backtrack(0)
        return [list(x) for x in res]