# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        ln = ListNode(object()) # sentinel
        tmp = ln

        l1, l2 = list1, list2


        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    tmp.next = ListNode(l1.val)
                    tmp = tmp.next
                    l1 = l1.next

                else:
                    tmp.next = ListNode(l2.val)
                    tmp = tmp.next
                    l2 = l2.next

            elif l1:
                tmp.next = ListNode(l1.val)
                tmp = tmp.next
                l1 = l1.next
            else:
                tmp.next = ListNode(l2.val)
                tmp = tmp.next
                l2 = l2.next

        return ln.next