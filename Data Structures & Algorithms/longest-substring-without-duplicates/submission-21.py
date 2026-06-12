class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import deque
        w = deque()
        longest = 0
        for r in range(len(s)):
            while s[r] in w:
                w.popleft()
            w.append(s[r])
            longest = max(longest, len(w))
        return longest

"""
- find the length of the longest substring without duplicate characters.
- a substring is a contiguous sequence of characters within a string.
- at a time the deque would only hold the unique characters of the string, hence it would
be O(m) space complexity at most. the non-unique ones would get popped out of the deque,
and hence they won't count in the space complexity.
- s[r] in w is an O(n) search, we need it to be O(1), hence we need to use a hashset.
"""