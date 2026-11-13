class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = ''
        l1, l2 = 0, 0
        n1, n2 = len(word1), len(word2)

        l1_turn = True

        while l1 < n1 or l2 < n2:
            if l1 < n1 and l2 < n2:
                if l1_turn:
                    res += word1[l1]
                    l1 += 1
                else:
                    res += word2[l2]
                    l2 += 1
                l1_turn = not l1_turn
            elif l1 < n1:
                res += word1[l1:]
                break
            else:
                res += word2[l2:]
                break

        return res