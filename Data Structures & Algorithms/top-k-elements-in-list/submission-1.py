class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        
        heap = []
        for num, freq in seen.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            else:
                if freq > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (freq, num))
        
        output = []
        for i in range(len(heap)):
            output.append(heap[i][1])
        
        return output



"""
- Create a Hashmap of num in the Key, and its frequency in Value.
- Have a minheap of k most frequent elements
- When you push a tuple onto a heap, the heap by default will sort
by the first element in the tuple. So the thing you want to sort,
make sure it is the 1st element of the tuple.
- First get it to k elements, and then you push and pop based on
values! But you will process each element and try to push it to
the heap
- Heap is just like a standard iterable python list. But it is not
sorted. However, the 0th index is guaranteed to be min/max value.
"""