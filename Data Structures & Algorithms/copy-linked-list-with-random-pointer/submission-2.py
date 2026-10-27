"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        from collections import defaultdict
        table = defaultdict(lambda: Node(0))
        table[None] = None

        tmp = head
        while tmp:
            table[tmp].val = tmp.val
            table[tmp].next = table[tmp.next]
            table[tmp].random = table[tmp.random]
            tmp = tmp.next

        return table[head]