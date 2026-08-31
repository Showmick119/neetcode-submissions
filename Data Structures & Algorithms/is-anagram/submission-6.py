class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        for char in s:
            sMap[char] = sMap.get(char, 0) + 1
        tMap = {}
        for char in t:
            tMap[char] = tMap.get(char, 0) + 1
        if sMap == tMap:
            return True
        return False

"""
- given 2 strings return true if the two strings are anagrams of each otherwise return False
- 2 strings are anagrams if they contain the same characters, with each character appearing
the same number of times.
- only the frequency of characters matters, not the order
"""