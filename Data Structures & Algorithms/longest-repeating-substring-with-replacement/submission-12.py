class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import deque
        w = deque()
        freq = {}
        maxFreq = 0
        longest = 0
        for r in range(len(s)):
            w.append(s[r])
            if s[r] not in freq:
                freq[s[r]] = 1
            else:
                freq[s[r]] += 1
            maxFreq = max(maxFreq, freq[s[r]])
            
            if len(w) - maxFreq <= k:
                longest = max(longest, len(w))
            else:
                w.popleft()
        return longest

"""
- Need to find valid windows, where after k replacements you have a string of only one
distinct character.
- From all the valid windows, find the window which is the largest.
- Since O(m) space is allowed, we can have a deque with the unique characters.
window_size - mostFreq <= k
- (5 - 3 <= 2), this is a valid window, as you could make 2 replacements, and have a full
string of 1 unique character.
- you can substract the most frequent character, and the remaining characters you could
replace and then get a string of just 1 character.
- the number of replacements needed has to be less than or equal to k. and remember it says
AT MOST k replacements, not at least k replacements.
"""