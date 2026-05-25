class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {}
        run = 0
        mp[run] = 1
        count = 0
        for num in nums:
            run += num
            if (run - k) in mp:
                count += mp[run - k]
            if run not in mp:
                mp[run] = 1
            else:
                mp[run] += 1
        return count
            

"""
- Create a running sum using a HashMap? But the running sum cannot be a total,
it has to be sum for each possible subarray.
- And we don't need the subarray itself, we just need the count, the number of
subarrays that there are.
- Key: Sum, Value: Count of Subarrays which had that Sum.
- Keep in mind that negative values are also possible, and this affects our
sum.
- If (current_sum - k) is seen somewhere else, that means there is a running
sum which equals to k.
- (current_sum - old_prefix = k), means there was some sequence of elements 
in between, that had a sum equal to k. And that is a valid subarray.
"""