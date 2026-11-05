# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # This is TLE
        # res = ListNode(object()) # SENTINEL delete this later
        # tmp = res
        # while any(lists):
        #     _fm = [(x.val, i) for (i, x) in enumerate(lists) if x]
        #     if not _fm:
        #         break
            
        #     _min = min(_fm)
        #     tmp.next = ListNode(_min[0])
        #     tmp = tmp.next

        #     lists[_min[-1]] = lists[_min[-1]].next


        # return res.next

        
        import heapq
        h = []
        for node in lists:
            while node:
                heapq.heappush(h, node.val)
                node = node.next

            
        res = ListNode(object())
        tmp = res
        while h:
            node = heapq.heappop(h)
            tmp.next = ListNode(node)
            tmp = tmp.next

        return res.next