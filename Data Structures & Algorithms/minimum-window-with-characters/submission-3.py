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
        
        bestLen = float("inf")
        bestL, bestR = 0, 0
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
                if (r - l + 1) < bestLen:
                    bestLen = r - l + 1
                    bestL, bestR = l, r
                if s[l].islower():
                    idx = ord(s[l]) - ord('a')
                    sFreq[idx] -= 1
                elif s[l].isupper():
                    idx = ord(s[l]) - ord('A')
                    idx += 26
                    sFreq[idx] -= 1
                l += 1
        if bestLen != float("inf"):
            out = s[bestL: bestR + 1]
            return out
        else:
            return ""

    def subsetCheck(self, sFreq: List[int], tFreq: List[int]) -> bool:
        """
        This is O(1) time complexity, even though it's a for-loop, because the for-loop is
        constant time, it does not rely on the size of any data structure and does the same
        amount of operation each time.
        """
        for i in range(52):
            if sFreq[i] < tFreq[i]:
                return False
        return True

"""
- always go naively at first
"""