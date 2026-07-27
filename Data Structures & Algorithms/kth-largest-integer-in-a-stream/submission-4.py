class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        import heapq
        self.heap = []
        self.k = k
        for num in nums:
            if len(self.heap) < self.k:
                heapq.heappush(self.heap, num)
            else:
                if self.heap[0] <= num:
                    smallest = heapq.heappop(self.heap)
                    heapq.heappush(self.heap, num)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            if self.heap[0] <= val:
                smallest = heapq.heappop(self.heap)
                heapq.heappush(self.heap, val)
        return self.heap[0]
        

"""
- find the kth largest integer from a stream of value, not necessarily just the largest
- so always keep and store the k largest in a certain order, such that you can easily pop and
get it
- stream of values is just a fancy term for array of data
- O(mlogk) time complexity and O(k) space, where m is the number of times add() was called,
and k represents the rank of the largest number to be tracked.
- always only keep upto k elements in the heap
"""