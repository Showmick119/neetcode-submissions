class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        w = 1
        i = 1
        count = 0
        while i < len(nums):
            if nums[i] == nums[w - 1]:
                count += 1
            else:
                nums[w] = nums[i] # w is the position for our next UNIQUE element
                # we have finally found a unique element, so we will do our swap and
                # increment w. this way we can continue and know that everything before w
                # is in its correct place and is only unique elements
                w += 1 # the element we just placed, we then compare with that and see if
                # i has a duplicate with it. because this w - 1 came from comparison with the
                # most recent i index. so if there's a match with the new i index, that means
                # there is another duplicate there with those i indexes!
            i += 1
        return len(nums) - count

"""
- everything before w has been processed and has the accurate unique elements!
- duplicates would be right next to each other since its sorted!
"""