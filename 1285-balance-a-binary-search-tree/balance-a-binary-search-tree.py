# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # cur, stack = root, []
        # res = []
        # while cur or stack:
        #     while cur:
        #         stack.append(cur)
        #         cur = cur.left
        #     cur = stack.pop()
        #     res.append(cur.val)
        #     cur = cur.right

        def inorder_traversal(node):
            if not node:
                return []
            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)

        sorted_array = inorder_traversal(root)
        
        def sorted_array_to_bBST(nums):
            if not nums:
                return None
            
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            
            root.left = sorted_array_to_bBST(nums[:mid])
            root.right = sorted_array_to_bBST(nums[mid+1:])
            
            return root
        
        return sorted_array_to_bBST(sorted_array)