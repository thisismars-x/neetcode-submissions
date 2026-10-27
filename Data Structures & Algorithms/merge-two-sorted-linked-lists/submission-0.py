# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        ll = ListNode()
        tmp = ll

        def _append_node(val):
            nonlocal tmp
            l2 = ListNode(val)
            tmp.next = l2
            tmp = tmp.next

        i = 0
        while list1 or list2:
            i += 1

            if list1 and list2:
                if list1.val > list2.val:
                    _append_node(list2.val)
                    list2 = list2.next
                else:
                    _append_node(list1.val)
                    list1 = list1.next

            elif list1:
                _append_node(list1.val)
                list1 = list1.next

            else:
                _append_node(list2.val)
                list2 = list2.next

        return ll.next

