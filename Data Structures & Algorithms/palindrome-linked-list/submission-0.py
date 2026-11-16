# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # the O(1) solution is to reverse the other half
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        if fast:
            slow = slow.next

        rcurr = slow
        rprev = None

        while rcurr:
            rcurr_next = rcurr.next
            rcurr.next, rprev = rprev, rcurr
            rcurr = rcurr_next

        curr = head
        while rprev:
            if rprev.val != curr.val:
                return False
            rprev = rprev.next
            curr = curr.next

        return True