class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        longest = 0

        table = {}

        start, end = 0, 0
        while end < n:
            table[s[end]] = table.get(s[end], 0) + 1

            while table[s[end]] > 1:
                table[s[start]] -= 1
                start += 1

            longest = max(longest, end - start + 1)
            end += 1

        return longest