class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for s in strs:
            freq = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                freq[idx] += 1
            freq = tuple(freq)
            if freq not in mp:
                mp[freq] = []
            mp[freq].append(s)
        out = []
        for key in mp:
            out.append(mp[key])
        return out

"""
- given an array of strings, group all anagrams together into sublists. you may return the
output in any order.
- an anagram is a string that contains the exact same characters as another string, but the
order of the characters can be different.
- we will definitely be using the ord() function here.
- every word can be represented as a list/tuple. now with a list and a tuple. one is mutable,
and another is immutable, so one can be used as a key to hashmap, which is the data structure
we will use, and another cannot be used as a key to a hashmap.
- tuple is immutable just like string, meaning you cannot change a specifix index and would just
have to create a brand new tuple for that.
- there's 26 letters in the alphabet.
- only lower case letters, so use ord('a'). if it was only upper case letters we would use
ord('A')
"""