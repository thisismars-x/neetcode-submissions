class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        
        from collections import deque
        d = deque((0,))

        farthest = 0

        while d:
            node = d.popleft()
            st = max(farthest + 1, node + minJump)
            for j in range(st, min(node + maxJump + 1, len(s))):
                if s[j] == '0':
                    d.append(j)
                    if j == len(s) - 1:
                        return True
            farthest = node + maxJump

        return False