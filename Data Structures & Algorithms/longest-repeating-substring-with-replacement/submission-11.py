class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import deque
        w = deque()
        freq = {}
        maxFreq = 0
        longest = 0
        l = 0 # shrink if the window is invalid
        for r in range(len(s)):
            w.append(s[r])
            if s[r] not in freq:
                freq[s[r]] = 1
            else:
                freq[s[r]] += 1
            maxFreq = max(maxFreq, freq[s[r]])
            w_size = len(w)
            if w_size - maxFreq <= k:
                longest = max(longest, w_size)
            else:
                w.popleft()
        return longest

"""
- keep track of windows, as well as the most frequent character in each window.
- we make multiple valid windows, and then we take the longest window.
"""