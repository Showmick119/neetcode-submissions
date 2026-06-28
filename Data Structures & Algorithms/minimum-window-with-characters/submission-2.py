class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        tFreq = [0] * 26 * 2
        for c in t:
            if c.islower():
                idx = ord(c) - ord('a')
                tFreq[idx] += 1
            elif c.isupper():
                idx = ord(c) - ord('A')
                idx += 26
                tFreq[idx] += 1
        
        candidates = []
        shortest = 0
        l = 0
        
        sFreq = [0] * 26 * 2
        for r in range(len(s)):
            # deque.append(s[r])
            if s[r].islower():
                idx = ord(s[r]) - ord('a')
                sFreq[idx] += 1
            elif s[r].isupper():
                idx = ord(s[r]) - ord('A')
                idx += 26
                sFreq[idx] += 1
            # deque.popleft() if condition satisfied
            while self.subsetCheck(sFreq, tFreq):
                candidates.append((r - l + 1, (l, r)))
                if s[l].islower():
                    idx = ord(s[l]) - ord('a')
                    sFreq[idx] -= 1
                elif s[l].isupper():
                    idx = ord(s[l]) - ord('A')
                    idx += 26
                    sFreq[idx] -= 1
                l += 1
        if len(candidates) > 0:
            candidates.sort(key=lambda x: x[0])
            l , r = candidates[0][1][0], candidates[0][1][1]
            out = s[l:r+1]
            if len(out) > 0:
                return out
            else:
                return ""
        else:
            return ""

    def subsetCheck(self, sFreq: List[int], tFreq: List[int]) -> bool:
        for i in range(52):
            if sFreq[i] < tFreq[i]:
                return False
        return True

"""
- always go naively at first
"""