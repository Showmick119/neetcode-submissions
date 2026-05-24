class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += str(len(s))
            output += '#'
            output += s
        return output
    
    def decode(self, s: str) -> List[str]:
        output = []
        curr = ""
        for i in range(len(s)):
            if s[i].isdigit() and s[i + 1] == '#':
                for j in range(int(s[i])):
                    curr += s[j + (i + 2)]
                output.append(curr)
                curr = ""
        return output

"""
- Encode a list of strings to a single string. This encoded string is then
sent over the network and decoded back to the original list of strings.
- There's 2 machines we are working with.
- Each method should be O(m) time-complexity, where m is the sum of lengths
of all the stringsand not just the number of strings, n.
- Machine 1 and 2 are completely seperate instances, and don't share any
memory.
- All the information has to be stored inside the encoded string itself,
such that it can be sent over the network.
- You need an encoding scheme that is self-contained.
- All the necessary information should already be in the String itself.
- The String returned should contain ALL strings in the list. Each string
should be seperated by some delimeter like #.
- Strings are immutable, so when you add to a string and change it, you create
a brand new String.
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