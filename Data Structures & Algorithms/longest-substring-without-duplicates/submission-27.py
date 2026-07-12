class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        from collections import deque
        window = deque()
        seen = set()
        l = 0
        longest = 0
        for idx in len(s):
            char = s[idx]
            if char not in seen:
                seen.add(char)
                window.append(char)
                longest = max(longest, len(window))
            else:
                while char in seen and l < len(s):
                    window.popleft()
                    seen.remove(s[l])
                    l += 1
                window.append(char)
        return longest

"""
- use hashsht for o(1) access of knowing if something exists
"""