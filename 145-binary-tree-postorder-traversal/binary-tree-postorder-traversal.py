# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack, visited = [], [root], [False]

        while stack:
            cur, v = stack.pop(), visited.pop()
            if cur:
                if v:
                    res.append(cur.val)
                else:
                    stack.append(cur)
                    visited.append(True)
                    stack.append(cur.right)
                    visited.append(False)
                    stack.append(cur.left)
                    visited.append(False)
        return res
        # if root:
        #     res.extend(self.postorderTraversal(root.left))
        #     res.extend(self.postorderTraversal(root.right))
        #     res.append(root.val)
        # return res