# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(root, pV, gpV):
            sum = 0
            if root == None:
                return 0
            if gpV % 2 == 0:
                sum = root.val
            
            sum += dfs(root.left, root.val, pV)
            sum += dfs(root.right, root.val, pV)
            return sum
        return dfs(root, 1, 1)