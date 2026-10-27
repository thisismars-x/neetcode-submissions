class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {')':'(', '}':'{', ']':'['}

        for char in s:
            if char in ('(', '[', '{'):
                stack.append(char)
            elif char in (')', ']', '}'):
                if stack and stack[-1] == table[char]:
                    stack.pop()
                    continue
                return False

        return True if not stack else False
