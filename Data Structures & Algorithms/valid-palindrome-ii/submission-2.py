class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        removed = False
        while l <= r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[r].lower() != s[l].lower():
                tempR = r - 1
                tempL = l + 1
                fixed = False
                if s[tempR].lower() == s[l].lower() and not removed:
                    fixed = True
                    removed = True
                    r = tempR
                    continue
                elif s[tempL].lower() == s[r].lower() and not removed:
                    fixed = True
                    removed = True
                    l = tempL
                    continue
                else:
                    return fixed
            l += 1
            r -= 1
        return True
        
"""
- Can s be a palindrome, after deleting at most 1 character from it?
- So you would remove while you are in the loop, but how do you know which
side to remove from?
- Use i + 1 and check ahead, that if removing it helps continue the palindrome
or not.
"""