class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for s in strs:
            chars = [0] * 26 # tuple representation of character freq of the string
            for c in s:
                chars[ord(c) - ord('a')] += 1 # count character frequency
            if tuple(chars) not in mp:
                mp[tuple(chars)] = [s]
            else:
                mp[tuple(chars)].append(s)
        out = []
        for key, value in mp.items():
            curr = []
            for val in value:
                curr.append(val)
            out.append(curr)
        return out

"""
- Lists are not hashable, hence not a valid key. But tuples are hashable and can be
used as keys in the map.
- The default thing is to use sorting. But that would bring the time complexity
higher than we want it to be. Hence, we sort with tuples and use the fact that
there's 26 letters in total.
- All of them are lowercase English letters.
- The final output data structure is required and does not count in our space comp
calculation, which only considers auxiliary space (Extra space used to solve the
problem).
- Remember they are all lowercase.
- Lowercase english letters start at 'a' in ASCII, and go all the way up to 'z'. So
it starts at ASCII value 97 and goes to 122.
- So ASCII value 97 ('a') would hold index 0 of our tuple, and ASCII value 122 ('z')
would hold index 25 of our tuple. But all in all it's a tuple of 26 elements.
"""