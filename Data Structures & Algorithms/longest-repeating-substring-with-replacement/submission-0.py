class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        start = end = 0

        max_len = 0

        count = {}
        while end < n:
            count[s[end]] = count.get(s[end], 0) + 1

            while (end - start + 1) - max(count.values()) > k:
                count[s[start]] -= 1
                if count[s[start]] == 0:
                    del count[s[start]]
                start += 1

            max_len = max(max_len, end - start + 1)

            end += 1

        return max_len

