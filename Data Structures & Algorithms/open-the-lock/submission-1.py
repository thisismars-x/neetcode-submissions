class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        
        # generate the solution tree and perform bfs to find min number of steps
        def children(l: int):
            res = []
            for i in range(4):
                dig = ( int(l[i]) + 1) % 10
                res.append(l[:i] + str(dig) + l[i + 1:])
                dig = ( int(l[i]) - 1 + 10 ) % 10
                res.append(l[:i] + str(dig) + l[i + 1:])
            return res

        from collections import deque 
        d = deque([("0000", 0)])
        visited = set(deadends)

        while d:
            node, turns = d.popleft()
            if node == target:
                return turns

            for child in children(node):
                if child not in visited:
                    visited.add(child)
                    d.append((child, turns + 1))

        return -1
