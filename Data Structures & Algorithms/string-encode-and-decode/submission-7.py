class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            size = len(s)
            out += str(size)
            out += '#'
            out += s
        return out 

    def decode(self, s: str) -> List[str]:
        out = []
        for i in range(len(s)):
            if s[i].isdigit() and s[i + 1] == '#':
                curr = ""
                for j in range(int(s[i])):
                    curr += s[i + 2 + j]
                out.append(curr)
        return out

"""
- Encoding should first show the length of the string and then a #, and then the string
itself.
Example: 4#jump3#cat
"""