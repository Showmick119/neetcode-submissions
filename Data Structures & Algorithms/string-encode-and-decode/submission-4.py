class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            size = len(s)
            output += str(size)
            output += '#'
            output += s
        return output
    
    def decode(self, s: str) -> List[str]:
        output = []
        curr = ""
        i = 0
        size = "" # can be 0 to 200 (so it can be 1 to 3 elements in the str)
        while i < len(s):
            if s[i].isdigit() and s[i + 1].isdigit() and s[i + 2].isdigit() and s[i + 3] == '#':
                num = int(s[i] + s[i + 1] + s[i + 2])
                for j in range(num):
                    curr += s[j + (i + 4)]
                output.append(curr)
                curr = ""
            elif s[i].isdigit() and s[i + 1].isdigit() and s[i + 2] == '#':
                num = int(s[i] + s[i + 1])
                for j in range(num):
                    curr += s[j + (i + 3)]
                output.append(curr)
                curr = ""
            elif s[i].isdigit() and s[i + 1] == '#':
                num = int(s[i])
                for j in range(num):
                    curr += s[j + (i + 2)]
                output.append(curr)
                curr = ""
            i += 1
        return output

"""
- Suppose the len is 10, we can't add 1 and then 0, as 1 + 0 = 1, and that's
incorrect and misleading.
- There can be upto 3 digits. So keep track of it somehow.
- Keep track of the 3 different situations: 3 digits of nums, 2 digits of nums,
1 digit of nums, followed by a #: 111#, 22#, 3#.
"""

"""
- To avoid the situation where we have input #, we should include the number
of characters that string has. Otherwise, decoding becoms ambigious, and it
becomes easy to get confused, as you don't know whether you should include the
# or not. As the # could well and truly be just a part of the string, as it
is one of the ASCII, so you can't so easily always rely on it to be your go to
delimter and let you know everything. You need another indicator too, to make up
for the fact that # is an ASCII character and can be part of the string, and isn't only
a delimeter.
- It needs to know to treat inner # as inner content, rather than a whole ass
seperator.
"""