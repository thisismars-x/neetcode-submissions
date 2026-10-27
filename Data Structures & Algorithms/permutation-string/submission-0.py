class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n, m = len(s1), len(s2)

        needed = {}
        for char in s1:
            needed[char] = needed.get(char, 0) + 1

        count = {}
        for char in s2[:n]:
            count[char] = count.get(char, 0) + 1


        from collections import Counter
        need = Counter(s1)

        for i in range(m - n + 1):
            if Counter(s2[i:i+n]) == need: return True

        return False