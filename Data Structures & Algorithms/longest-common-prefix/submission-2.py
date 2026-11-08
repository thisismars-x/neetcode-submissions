class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        end = 0

        for i in range(len(strs[0])):
            char = strs[0][i]

            for s in strs[1:]:
                if not (i < len(s)) or s[i] != char:
                    return strs[0][:end]

            end += 1

        return strs[0][:end]


        