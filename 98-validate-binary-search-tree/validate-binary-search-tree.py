# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def rec(node, left, right):
            if node:
                if node.val <= left or node.val >= right: return False
                return rec(node.left, left, node.val) and rec(node.right, node.val, right)
            return True
        return rec(root, -float('inf'), float('inf') )