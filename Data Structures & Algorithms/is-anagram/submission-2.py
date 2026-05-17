class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        newS = "".join(sorted(s))
        newT = "".join(sorted(t))
        if newS == newT:
            return True
        return False