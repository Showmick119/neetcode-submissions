class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        c1 = [0] * 26
        for r in range(len(s1)):
            idx = ord(s1[r]) - ord('a')
            c1[idx] += 1
        
        l = 0 # idx of the left char of the deque (sliding window behavior)
        c2 = [0] * 26
        for r in range(len(s2)):
            idx = ord(s2[r]) - ord('a')
            c2[idx] += 1
            if (r + 1) >= len(s1):
                if c1 == c2:
                    return True
                else:
                    idx = ord(s2[l]) - ord('a')
                    c2[idx] -= 1 # such that we only have the frequency counts of the latest deque
                    l += 1
        return False

"""
- whenever we reach number that is giving us a length that is comparable to the s1's length,
we create 2 more temporary pointers and do a letter by letter comparison.
- you can use data structures, but it can't be something whose size grows as the code
progresses, it must have a fixed size.
- we don't need tuples, since there is no use of hashing here. equal length list and same
order of elements will lead to the lists being the same.
- we need sliding window behavior, where we add right character and we remove left character.
- we don't need a deque, we just need a left pointer, and a right pointer.
"""