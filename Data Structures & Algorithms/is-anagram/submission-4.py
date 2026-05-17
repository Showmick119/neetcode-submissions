class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sMap = {}
        tMap = {}

        # O(n)
        for i in range(len(s)):
            curr = s[i]
            if curr not in sMap:
                sMap[curr] = 1
            else:
                sMap[curr] += 1
        
        # O(m)
        for i in range(len(t)):
            curr = t[i]
            if curr not in tMap:
                tMap[curr] = 1
            else:
                tMap[curr] += 1
        
        for key in sMap:
            if key not in tMap:
                return False
            if sMap[key] != tMap[key]:
                return False
        return True


"""
- Create 2 seperate HashMaps.
- 1 HashMap for each String s and another for t.
- After creating these HashMaps, go through their key (character),
and check with the other HashMap's key, and whether they store the
same value, that being the quantity of times the character showed
up.
- HashMap Key: Character
- HashMap Value: Quantity Of Times It Shows Up
"""