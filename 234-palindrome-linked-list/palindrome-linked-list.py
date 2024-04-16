# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''learning a lot here, to divide the linked list into 
        we use two pointers to the head. Then we reverse the 
        second half and check for palindrome
        '''

        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # the above code takes slow to the middle of the linked list
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        #check for palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True
