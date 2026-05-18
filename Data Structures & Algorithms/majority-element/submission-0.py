class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        req = n // 2
        count = 0
        leader = nums[0] ## pick something
        for num in nums:
            if num == leader:
                count += 1
            else:
                count -= 1
                if count < 0:
                    leader = num
                    count = 0
        return leader


"""
- We need to one-pass and only rely on temporary variables!
- Keep a leader and a quantity of times it shows up.
- Each time you see something that is not the leader, you reduce
it's count. In the end you only keep the leader which has a count.
- This is the Boyer Moore pattern, and this will work only because
the majority element appears more than (n // 2) times.
"""