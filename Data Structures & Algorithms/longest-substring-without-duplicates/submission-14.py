class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import deque
        w = deque()
        longest = 0
        for c in s:
            while c in w:
                w.popleft()
            w.append(c)
            longest = max(longest, len(w))
        return longest

"""
- Find the length of the longest substring without duplicate characters.
- A substring is a contiguous sequence of characters within a string.
- O(n) time, so visit every element only once for every element.
- O(m) space, so you can keep a window of m unique characters, as you slide across all the
characters.
"""