class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1
        while l <= r: ## can swap l and r, even when they are same index
            # not a problem per say
            temp = s[r]
            s[r] = s[l]
            s[l] = temp
            l += 1
            r -= 1

"""
- Very obviously a 2-pointers problem.
"""