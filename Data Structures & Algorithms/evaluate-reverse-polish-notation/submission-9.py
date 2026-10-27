class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for lex in tokens:
            if (lex[0] == "-" and lex[1:].isdecimal()) or lex.isdecimal():
                stack.append(int(lex))
            else:
                right, left = stack.pop(), stack.pop()
                match lex:
                    case "+":
                        stack.append(left + right)
                    case "-":
                        stack.append(left - right)
                    case "*":
                        stack.append(left * right)
                    case "/":
                        stack.append(int(left / right))
        
        return int(stack.pop())