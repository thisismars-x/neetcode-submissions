class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        table = {
            '2': "abc", '3': "def", '4': "ghi",
            '5': "jkl", '6': "mno", '7': "pqrs",
            '8': "tuv", '9': "wxyz",
        }

        if not digits:
            return []
        if len(digits) == 1:
            return [c for c in table[digits]]

        def find_cartesian(w1: str, w2: str) -> list[str]:
            result = []

            for c1 in w1:
                for c2 in w2:
                    result.append(c1 + c2)

            return result

        result = table[digits[0]]

        for digit in digits[1:]:
            result = find_cartesian(result, table[digit])

        return result