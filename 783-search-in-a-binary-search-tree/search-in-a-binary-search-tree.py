# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def find(root: Optional[TreeNode]) -> Optional[TreeNode]:
            if root is None: return None
            if val == root.val: return root
            if val < root.val: return find(root.left)
            if val > root.val: return find(root.right)

        return find(root)
        # res = []
        # def traverse(cur: Optional[TreeNode]):
        #     if cur:
        #         res.append(cur.val)
        #         res.extend(traverse(cur.left))
        #         res.extend(traverse(cur.right))
        # return res

