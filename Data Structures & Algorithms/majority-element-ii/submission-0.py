class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        output = []
        req = len(nums) // 3
        leader = nums[0]
        count = 0
        for num in nums:
            if num == leader:
                count += 1
                if count > req:
                    output.append(leader)
            else:
                count -= 1
                if count == 0:
                    leader = num
        return output

"""
- In Majorityn Element I, we kept a leader and it's count. Since the majority
comes up so many times, that by the end of it, it would still remain a leader,
even though you would deduct from its count, everytime you saw a non-leader.
- Apply the same concept of leader and count, but leader added to list, only
if count exceed a certain threshold.
"""