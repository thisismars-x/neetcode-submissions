class Solution:
    def decodeString(self, s: str) -> str:

        char_stack, count_stack = [], []
        
        k = 0
        curr = ''
        for char in s:
            if char.isdigit():
                k = k * 10 + int(char)
            elif char == '[':
                char_stack.append(curr)
                count_stack.append(k)
                curr = ''
                k = 0
            elif char == ']':
                tmp = curr
                curr = char_stack.pop()
                count = count_stack.pop()
                curr += tmp * count
            else:
                curr += char

        return curr
