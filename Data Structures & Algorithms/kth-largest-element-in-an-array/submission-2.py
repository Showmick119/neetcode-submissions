class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                if heap[0] <= num:
                    smallest = heapq.heappop(heap)
                    heapq.heappush(heap, num)
        return heap[0]

"""
- given an unsorted array of integers nums and an integer k
- return the kth largest element in the array
- and it should be the kth largest element in the sorted order, not the kth distinct element
"""