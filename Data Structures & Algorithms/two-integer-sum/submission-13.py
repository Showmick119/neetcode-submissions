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