class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        from collections import Counter
        need = Counter(s1)

        for i in range(m - n + 1):
            if Counter(s2[i:i+n]) == need: return True

        return False