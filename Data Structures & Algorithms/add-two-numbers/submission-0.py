# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        number1 = ""
        number2 = ""
        
        tmp1, tmp2 = l1, l2
        while tmp1:
            number1 += str(tmp1.val)
            tmp1 = tmp1.next

        while tmp2:
            number2 += str(tmp2.val)
            tmp2 = tmp2.next

        number1 = int(number1[::-1])
        number2 = int(number2[::-1])
        result = str(number1 + number2)[::-1]

        ll = ListNode(0)
        tmp = ll
        for char in result:
            tmp.next = ListNode(int(char))
            tmp = tmp.next

        return ll.next
            