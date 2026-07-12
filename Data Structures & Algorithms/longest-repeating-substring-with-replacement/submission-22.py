class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import deque
        window = deque()
        longest = 0
        mostFreq = 0
        l = 0 # idx
        mp = {}
        for char in s:
            window.append(char)
            if char not in mp:
                mp[char] = 1
            else:
                mp[char] += 1
            mostFreq = max(mostFreq, mp[char])
            if len(window) - mostFreq <= k:
                longest = max(longest, len(window))
            else:
                mp[s[l]] -= 1
                l += 1
                window.popleft()
        return longest

"""
- need to keep track of valid substrings which meet a certain condition.
"""