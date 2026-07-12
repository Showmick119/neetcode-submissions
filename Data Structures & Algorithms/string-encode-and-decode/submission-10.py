class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            curr = ""
            size = len(string)
            curr += str(size)
            curr += "#"
            curr += string
            encoded += string
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        curr_size = "" # in case the digit is greater than 9
        final_size = 0
        i = 0
        while i < len(s):
            char = s[i]
            if char.isdigit():
                curr_size += char
            elif char == "#":
                final_size = int(curr_size)
                curr_string = s[(i + 1):(i + final_size + 1)]
                i += final_size + 1
                decoded.append(curr_string)
        return decoded


"""
- encode a list of strings to a string
- the encoded string is then sent over the network and decoded back to the original list
of strings
- stringLength#string: 5#Hello
"""