class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import deque
        window = deque()
        longest = 0
        mostFreq = 0
        mp = {}
        for char in s:
            if char not in mp:
                mp[char] = 1
            else:
                mp[char] += 1
            mostFreq = max(mostFreq, mp[char])
            window.append(char)
            if len(window) - mostFreq <= k: # means its a valid substring
                longest = max(longest, len(window))
            else:
                window.popleft()
        return longest

"""
- need to keep track of valid substrings which meet a certain condition.

"""