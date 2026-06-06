class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import deque
        w = deque()
        seen = set()
        longest = 0
        for c in s:
            while c in seen:
                seen.remove(w[0])
                w.popleft()
            w.append(c)
            seen.add(c)
            longest = max(longest, len(w))
        return longest

"""
- Find the length of the longest substring without duplicate characters.
- A substring is a contiguous sequence of characters within a string.
- O(n) time, so visit every element only once for every element.
- O(m) space, so you can keep a window of m unique characters, as you slide across all the
characters.
- You can use deque() as both a LIFO Stack, and as a FIFO Queue, but have O(1) operations
for all the adding/removing from the front/back.
"""