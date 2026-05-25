class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l <= r:
            if s[r] != s[l]:
                # trying both options (removing from left side or right side)
                # if even one successful path is possible from here, we continue
                # exploring the palindrome

                # we are no longer restricting and searching just one side, but rather
                # considering both. if either path tells us we should continue, and that
                # palindrome exists from here, then we can continue

                # if palindrome does not exist from here onwards, then return False
                # and stop searching entirely
                if not self.isPalindrome(s[l:r]) and not self.isPalindrome(s[l+1:r+1]):
                    return False
            l += 1
            r -= 1
        return True
    
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False
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