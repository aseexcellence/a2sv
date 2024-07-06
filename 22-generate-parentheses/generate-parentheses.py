class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        IDENtify the three base cases
        1. Only add open parentheses if the #( is less than n
        2. Only add a closing parentheses if the #) is less than #(
        3. We have valid parentheses IFF #( == #) == n
        """
        stack = []
        res = []

        def backtrack(openP, closedP):
            if openP == closedP == n:
                res.append("".join(stack))
                return
            
            if openP < n:
                stack.append("(")
                backtrack(openP + 1, closedP)
                stack.pop()

            if closedP < openP:
                stack.append(")")
                backtrack(openP, closedP + 1)
                stack.pop()

        backtrack(0, 0)
        return res