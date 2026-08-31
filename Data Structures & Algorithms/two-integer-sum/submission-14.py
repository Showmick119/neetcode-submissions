class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for index, num in enumerate(nums):
            mp[num] = index # keep the latest ones, as the earlier ones will be processed in
            # the next loop
        for index, num in enumerate(nums):
            if target - num in mp:
                if index != mp[target - num]:
                    if index < mp[target - num]:
                        return [index, mp[target - num]]
                    else:
                        return [mp[target - num], index]
        return []

"""
- think about how hashing techniques can be applied, as it will make searching and lookup
times into O(1), rather than the O(n) searching and lookup times in arrays and linked lists
- since the 2nd loop checks every index, it doesn't matter if the 1st loop stored the earliest
or latest index, as ultimately it will skip over the duplicate indexes when going through all
of them, regardless of if the earlier or latest was stored.
"""