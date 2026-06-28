class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        # tFreq = [0] * 26 * 2 # frequency of all characters in small string t
        # for c in t:
        #     if c.islower():
        #         idx = ord(c) - ord('a')
        #         tFreq[idx] += 1
        #     elif c.isupper():
        #         idx = ord(c) - ord('A')
        #         idx += 26 # to push it to the uppercase portions
        #         tFreq[idx] += 1
        # from collections import deque
        # w = deque()
        # indices = deque()
        # stack = [] # will only store the shortest pair of indices
        # shortest = 0
        # l = 0
        # sFreq = [0] * 26 * 2
        # for r in range(len(s)):
        #     if s[r].islower():
        #         idx = ord(s[r]) - ord('a')
        #         sFreq[idx] += 1
        #     elif s[r].isupper():
        #         idx = ord(s[r]) - ord('A')
        #         idx += 26 # to push it to the uppercase portions
        #         sFreq[idx] += 1
        #     deque.append(s[r])

        #     if sFreq == tFreq:
        #         pass
        # l, r = stack[-1][0], stack[-1][1]
        # out = s[l:r]
        # if len(out) > 0:
        #     return out
        # else:
        #     return ""
        from collections import deque, Counter
        w = deque()
        candidates = []
        shortest = 1000000000
        for r in s:
            w.append(r)
            while Counter(w) >= Counter(t):
                shortest = min(shortest, len(w))
                candidates.append((len(w), "".join(w)))
                w.popleft()
        if len(candidates) > 0:
            candidates.sort(key=lambda x: x[0]) # smallest to largest by default
            out = "".join(candidates[0][1])
            return out
        else:
            return ""

"""
- always go naively at first
"""