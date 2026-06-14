class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        from collections import deque
        w = deque()
        for r in range(len(s2)):
            w.append(s2[r])
            if len(w) == len(s1):
                if "".join(sorted(w)) == "".join(sorted(s1)):
                    return True
                else:
                    w.popleft()
        return False

"""
- whenever we reach number that is giving us a length that is comparable to the s1's length,
we create 2 more temporary pointers and do a letter by letter comparison.
"""