class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        req = len(nums) // 3
        output = set()
        if len(nums) == 1:
            output.add(num)
            return list(output)
        mp = {}
        for num in nums:
            if num not in mp:
                mp[num] = 1
                if mp[num] > req:
                    output.add(num)
            else:
                mp[num] += 1
                if mp[num] > req:
                    output.add(num)
        return list(output)

"""
- In Majorityn Element I, we kept a leader and it's count. Since the majority
comes up so many times, that by the end of it, it would still remain a leader,
even though you would deduct from its count, everytime you saw a non-leader.
- Apply the same concept of leader and count, but leader added to list, only
if count exceed a certain threshold.
- This Boyer-Moore Voting techniques works only for single element. For
multiple elements it falls short.
"""