class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {}
        run = 0
        count = 0
        mp[0] = 1
        for num in nums:
            if run not in mp:
                mp[run] = 1 # one sub array which has this sum. and prefix sums are sum of elements before that particular index i
            else:
                mp[run] += 1
            if run - k in mp:
                count += mp[run - k]
            run += num
        return count

"""
- prefixSum[i] - prefixSum[j] = k
- prefixSum[i] - k = prefixSum[j], then the subarray betwen indices i and j are also equal
to k.
- Store the subarray sums as keys in the map, and then the value should be there quantity.
"""