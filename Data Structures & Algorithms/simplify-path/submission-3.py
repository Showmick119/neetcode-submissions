class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        stack.append("")
        for p in path:
            if len(p) == 0:
                continue
            elif p == '.': # you stay at the current directory, you don't add nor remove
                continue
            elif p == '..':
                if len(stack) > 1:
                    stack.pop()
            else:
                stack.append(p)
        # Edge Case
        if len(stack) == 1 and stack[-1] == "":
            return "/"
        output = '/'.join(stack)
        return output