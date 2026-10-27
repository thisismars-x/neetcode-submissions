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

        table = {None: None}

        tmp = head
        while tmp:
            table[tmp] = Node(tmp.val)
            tmp = tmp.next
        
        tmp = head
        while tmp:
            _copy = table[tmp]
            _copy.next, _copy.random = table[tmp.next], table[tmp.random]
            tmp = tmp.next

        return table[head]
