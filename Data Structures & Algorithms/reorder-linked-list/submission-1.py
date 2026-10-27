# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # lets solve by bruting
        # nodes = []
        # tmp = head
        # while tmp:
        #     nodes.append(tmp)
        #     tmp = tmp.next

        # i, j = 0, len(nodes) - 1

        # while i < j:
        #     nodes[i].next = nodes[j]
        #     i += 1
        #     if i == j: break

        #     nodes[j].next = nodes[i]
        #     j -= 1

        # nodes[i].next = None

        # first find midpoint
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow is at mdpt
        prev = None
        curr = slow.next

        slow.next = None

        # reverse the upper half
        while curr:
            after_curr = curr.next
            curr.next = prev
            prev, curr = curr, after_curr

        first, second = head, prev
        while second:
            t1, t2 = first.next, second.next
            first.next, second.next = second, t1
            first, second = t1, t2
