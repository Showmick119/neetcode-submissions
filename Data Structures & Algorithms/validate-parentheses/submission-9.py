class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        if len(s) == 1:
            return False
        for c in s:
            if c in mp:
                if stack[-1] not in mp:
                    if stack[-1] != mp[c]:
                        return False
                    else:
                        stack.pop()
            else:
                stack.append(c)
        return True

"""
- you are given a string s consisting of certain outlined characters.
- the string is valid if every open bracket is closed by the same type of close bracket.
- open brackets are closed in the correct order.
- every close bracket has a corresponding open bracket of the same type.
- o(n) time and space
"""