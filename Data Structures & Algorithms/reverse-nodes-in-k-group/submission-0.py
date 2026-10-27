# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    
 
        length = 0
        tmp = head
        while tmp:
            length += 1
            tmp = tmp.next
    
        from math import ceil
        n_groups = int(ceil(length / k))
    
        groups = [None] * n_groups
    
        tmp = head
        for i in range(n_groups):
            tmp2 = tmp
            for j in range(k - 1):
                if not tmp2: break
                tmp2 = tmp2.next
    
            temp = tmp2.next if tmp2 else None
            if tmp2: tmp2.next = None
            groups[i] = tmp
            tmp = temp
    
        # reverse each group
        for i in range(n_groups):
            curr, prev = groups[i], None
            # check if this group is exactly k elem
            length_ = 0
            tmps = curr
            while tmps:
                length_ += 1
                tmps = tmps.next
    
            if length_ != k: break
    
    
            while curr:
                after_curr = curr.next
                curr.next = prev
                curr, prev = after_curr, curr
            groups[i] = prev
    
        for i in range(n_groups):
            tmp = groups[i]
            while tmp.next:
                tmp = tmp.next
    
            if i != n_groups - 1:
                tmp.next = groups[i + 1]
    
        return groups[0]