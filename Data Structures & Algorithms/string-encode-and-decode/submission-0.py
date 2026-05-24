class Solution:
    mp = {} # static variable variable

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += s
            output += "#"
        return output
    
    def decode(self, s: str) -> List[str]:
        output = []
        curr = ""
        for char in s:
            if char == "#":
                output.append(curr)
                curr = ""
            else:
                curr += char
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
"""