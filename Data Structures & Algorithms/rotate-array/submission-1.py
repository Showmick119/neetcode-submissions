class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        l = 0
        r = len(nums) - 1
        if k > len(nums):
            k = k % len(nums)
        while l <= r and count != k:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
            count += 1
        size = len(nums)
        nums[0:k] = reversed(nums[0:k])
        nums[k:size] = reversed(nums[k:size])
        

"""
- Every rotation is just simply bringing the element at the back, to the front.
- Keep 2 pointers, one for element being bought to the front, and one for the
element.
- We require a time complexity of O(n), and a space complexity of O(1). A time
complexity of O(n * k) would be the naive approach.
- Do it all in ONE GO!!!!! Instead of moving to the right one-by-one. Just move all
at once!
- But we would overwrite. What's the solution to that problem? We can't even
introduce any new data structures. So what do we do?
- Reverse, and then for the final k placed elements, fix their order.
"""