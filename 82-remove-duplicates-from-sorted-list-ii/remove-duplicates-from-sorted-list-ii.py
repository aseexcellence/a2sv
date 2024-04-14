# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next
        
        # Edge case where the list might be empty
        if not head:
            return head

        # Sentinel node to handle edge cases such as removing the head node
        sentinel = ListNode(0, head)
        predecessor = sentinel

        while head:
            # If it's the beginning of duplicates substring
            if head.next and head.val == head.next.val:
                # Move till the end of duplicates substring
                while head.next and head.val == head.next.val:
                    head = head.next
                # Skip all duplicates
                predecessor.next = head.next
            else:
                # Otherwise, move predecessor
                predecessor = predecessor.next

            # Move forward
            head = head.next

        return sentinel.next
