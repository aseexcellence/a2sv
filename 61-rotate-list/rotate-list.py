# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        size = 1
        tail = head
        while tail.next:
            tail = tail.next
            size += 1
        k = k % size
        if k == 0:
            return head
        cut = head
        n = size - k - 1
        while n > 0:
            cut = cut.next
            n -= 1
        newHead = cut.next
        cut.next = None
        tail.next = head
        return newHead

        
