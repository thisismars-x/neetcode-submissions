class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #stupid
        from collections import Counter
        return Counter(s) == Counter(t)