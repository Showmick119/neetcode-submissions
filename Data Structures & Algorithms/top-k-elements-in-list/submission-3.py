class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out = []
        mp = {}
        for num in nums:
            if num not in mp:
                mp[num] = 1
            else:
                mp[num] += 1
        
        for i in range(k):
            curr, val = max(mp.items(), key=lambda x: x[1])
            mp[curr] = 0
            out.append(curr)
        return out

"""
- O(n) time and space complexity.
"""