class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for num in nums:
            if num not in mp:
                mp[num] = 1
            else:
                mp[num] += 1
        output = []
        for i in range(k):
            key = max(mp, key=mp.get)
            output.append(key)
            mp[key] = 0
        return output

"""
- k most frequent elements within an array, which can be returned in any order.
- Only one pass through the array, so time-comp of O(n).
- Can only make one data structure storing n elements.
- Total space generally also counts in the returned data structure, whereas
auxiliary space counts only the temporary extra memory used, and excludes
output data structure.
"""