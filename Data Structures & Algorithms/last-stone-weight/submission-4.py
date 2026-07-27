class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return 0
        import heapq
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        while len(heap) > 1:
            n1 = abs(heapq.heappop(heap))
            n2 = abs(heapq.heappop(heap))
            if n1 != n2:
                n3 = abs(n1 - n2)
                heapq.heappush(heap, -n3)
        if len(heap) == 0:
            return 0
        else:
            return abs(heap[0])

"""
- store negative values for maxheap purposes
"""