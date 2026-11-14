class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for parts in path.split('/'):
            if parts in ('', '.'):
                continue

            if parts == '..':
                if stack:
                    stack.pop()

            else:
                stack.append(parts)

        return '/' + '/'.join(stack)
    
                