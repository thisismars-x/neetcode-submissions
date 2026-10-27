# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # my solution uses too many assumptions

        # if not head or not head.next: return head
        # prev, curr = head, head.next
        # prev.next = None

        # while curr:
        #     after_curr = curr.next
        #     curr.next = prev
        #     curr, prev = after_curr, curr

        # return prev

        prev = None
        curr = head

        while curr:
            after_curr = curr.next
            curr.next = prev
            curr, prev = after_curr, curr

        return prev
