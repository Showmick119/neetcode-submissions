class Solution:
    def simplifyPath(self, path: str) -> str:
        items = path.split('/')
        stack = []
        for i in items:
            if i == '':
                continue
            elif i == '.':
                continue
            elif i == '..':
                if len(stack) > 0:
                    stack.pop() # remove prev item
            else:
                stack.append(i)
        out = "/" + "/".join(stack)
        return out