class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)

        need = len(count1)
        for i in range(len(s2)):
            count2, cur = {}, 0
            for j in range(i, len(s2)):
                count2[s2[j]] = 1 + count2.get(s2[j], 0)
                if count1.get(s2[j], 0) < count2[s2[j]]:
                    break
                if count1.get(s2[j], 0) == count2[s2[j]]:
                    cur += 1
                if cur == need:
                    return True
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