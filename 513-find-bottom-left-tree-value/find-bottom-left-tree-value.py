# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        '''
        Traverse in BFS algorithm from right to left and return the 
        last node value. We are gonna use deque here.
        '''
        q = deque([root])

        while q:
            node = q.popleft()

            if node.right: q.append(node.right)
            if node.left: q.append(node.left)
        return node.val