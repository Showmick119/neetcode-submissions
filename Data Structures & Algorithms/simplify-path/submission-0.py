class Solution:
    def simplifyPath(self, path: str) -> str:
        files = path.split('/') # creates a list of strings which ae split by the slashes
        stack = []
        for f in files:
            if f == '':
                continue
            elif f == '.':
                continue
            elif f == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(f)
        out = "/" + "/".join(stack)
        return out

"""
- return the simplified path which begins with '/'. your task is to transform
googledata/gws/experiments/mendel/gws/studies/shopping/help_me_pick_gws_coordinated_study.gcl
- 
"""