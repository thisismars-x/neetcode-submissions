class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        nhead = ListNode(-1, head)

        before = nhead
        for _ in range(left - 1):
            before = before.next

        curr = before.next
        tail = curr
        prev = None

        for _ in range(right - left + 1):
            after_curr = curr.next
            curr.next = prev
            prev = curr
            curr = after_curr

        before.next = prev
        tail.next = curr

        return nhead.next