class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
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
- you are given 2 strings s1 and s2, return true if s2 (the larger string) contains a
permutation of s1 (the smaller string) as its substring.
- a permutation is a rearrangement of the same elements. but when those same elements are
sorted, that arrangement becomes the same and the permutations become equal.
- go through s2, and each time you have a window that is equal in length to the s1 string.
sit down and compare them. if same permutation return true, if not, cut from the back, and
add to the front and keep going over the s2.
- we need to aim for o(n) time comp and o(1) space comp. how do we check for permutation
between 2 strings? do a 2 pointers a frequency count? but that would need another data
structure? start of with the naive solution
"""