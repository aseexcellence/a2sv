# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack1 = []
        stack2 = []
        def p_recur(p: Optional[TreeNode]):
            if p:
                stack1.append(p.val)
                p_recur(p.left)
                p_recur(p.right)
            else: stack1.append(None)
        def q_recur(q: Optional[TreeNode]):
            if q:
                stack2.append(q.val)
                q_recur(q.left)
                q_recur(q.right)
            else: stack2.append(None)

        p_recur(p)
        q_recur(q)
        return stack1 == stack2


        