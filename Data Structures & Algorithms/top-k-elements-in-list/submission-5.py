class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for num in nums:
            if num in freqMap:
                freqMap[num] += 1
            else:
                freqMap[num] = 1
        freqList = [[] for _ in range(len(nums) + 1)]
        for num, idx in freqMap.items():
            freqList[idx].append(num)
        out = []
        for fList in reversed(freqList):
            for item in fList:
                if len(out) == k:
                    return out
                else:
                    out.append(item)
        return out

"""
- given an integer array nums and an integer k, return the k most frequent elements within the
array.
- you may return the output in any order.
- o(n) time and space complexity.
- 
"""