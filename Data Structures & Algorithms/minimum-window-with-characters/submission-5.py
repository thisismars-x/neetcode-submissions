class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        if not s or not t:
            return ""

        needed = Counter(t)
        current = Counter()

        required = len(needed)
        have = 0

        start = 0
        min_start = 0
        min_len = float("inf")

        for end, char in enumerate(s):
            if char in needed:
                current[char] += 1

                if current[char] == needed[char]:
                    have += 1

            while have == required:
                curr_len = end - start + 1

                if curr_len < min_len:
                    min_len = curr_len
                    min_start = start

                left = s[start]

                if left in needed:
                    if current[left] == needed[left]:
                        have -= 1

                    current[left] -= 1

                start += 1

        if min_len == float("inf"):
            return ""

        return s[min_start:min_start + min_len]