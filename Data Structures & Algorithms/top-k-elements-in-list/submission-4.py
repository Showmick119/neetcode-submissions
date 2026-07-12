class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1
        freq_list = [[] for _ in range(len(nums) + 1)]
        for key, value in hash_map.items():
            freq_list[value].append(key)
        idx = len(nums)
        output = []
        while k > 0 and idx > 0:
            if len(freq_list[idx]) > 0:
                while len(freq_list[idx]) > 0 and k > 0:
                    output.append(freq_list[idx].pop())
                    k -= 1
            else:
                idx -= 1
        return output

"""
- create an array of arrays, where the frequency determines the array we are currently on
"""