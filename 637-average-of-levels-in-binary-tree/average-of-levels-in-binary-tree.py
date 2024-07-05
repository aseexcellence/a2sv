# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        Q = deque()
        Q.append(root)
        
        while Q:
            level_sum = 0
            q_size = len(Q)

            for _ in range(q_size):
                node = Q.popleft()
                level_sum += node.val
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            
            avg = level_sum / q_size
            res.append(avg)
        
        return res
            