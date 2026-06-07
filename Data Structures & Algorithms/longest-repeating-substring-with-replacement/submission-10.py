class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import deque
        w = deque()
        freq = {}
        maxFreq = 0
        l = 0
        longest = 0
        for r in range(len(s)):
            if s[r] not in freq:
                freq[s[r]] = 1
            else:
                freq[s[r]] += 1
            maxFreq = max(maxFreq, freq[s[r]])

            while (r - l + 1) - maxFreq > k:
                freq[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest