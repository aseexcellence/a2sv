"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        _new = {}
        
        cur = head
        while cur:
            _new[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            _new[cur].next = _new.get(cur.next)
            _new[cur].random = _new.get(cur.random)
            cur = cur.next
            
        return _new[head]
        