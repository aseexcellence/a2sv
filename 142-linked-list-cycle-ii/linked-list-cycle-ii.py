# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        slow, fast = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        
        if not fast.next or not fast.next.next:
            return
        slow2 = head
        while slow.next:
            if slow == slow2:
                return slow
            slow2 = slow2.next
            slow = slow.next