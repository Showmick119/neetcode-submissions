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
        i = 0
        curr = ""
        size = ""
        while i < len(s):
            if s[i].isdigit(): # assuming it starts with a number always
                size += s[i]
                i += 1
                continue
            elif s[i] == '#':
                num = int(size)
                for j in range(num):
                    curr += s[j + (i + 1)]
                output.append(curr)
                curr = ""
                size = ""
                i += (num + 1)
        return output

"""
- Suppose the len is 10, we can't add 1 and then 0, as 1 + 0 = 1, and that's
incorrect and misleading.
- There can be upto 3 digits. So keep track of it somehow.
- Keep track of the 3 different situations: 3 digits of nums, 2 digits of nums,
1 digit of nums, followed by a #: 111#, 22#, 3#.
- Keep reading numbers until you find a #.
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