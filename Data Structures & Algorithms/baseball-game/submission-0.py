class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []

        for op in operations:
            match op:
                case '+':
                    stack.append(stack[-2] + stack[-1])

                case 'D':
                    stack.append(stack[-1] * 2)

                case 'C':
                    stack.pop()

                case num:
                    stack.append(int(num))

        return sum(stack)