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
        curr = ""
        size = ""
        i = 0
        while i < len(s):
            if s[i].isdigit():
                size += s[i]
                i += 1
                continue
            elif s[i] == '#':
                num = int(size)
                for j in range(num):
                    curr += s[j + i + 1]
                out.append(curr)
                i += num + 1
                curr = ""
                size = ""
        return out

"""
- Encoding should first show the length of the string and then a #, and then the string
itself.
Example: 4#jump3#cat
"""