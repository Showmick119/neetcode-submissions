class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import deque
        window = deque()
        seen = set()
        l = 0
        longest = 0
        for char in s:
            if char not in seen:
                seen.add(char)
                longest = max(longest, len(window))
            else:
                while char in seen:
                    window.popleft()
                    seen.remove(s[l])
                    l += 1
            window.append(char)
        return longest

"""
- use hashsht for o(1) access of knowing if something exists
"""