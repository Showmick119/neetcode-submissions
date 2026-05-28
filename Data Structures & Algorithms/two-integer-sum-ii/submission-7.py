class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            if (numbers[l] + numbers[r]) < target:
                l += 1
            elif (numbers[l] + numbers[r]) > target:
                r -=1
            else:
                return [l + 1, r + 1]

"""
- Have to use 2 Pointers somehow, but don't exactly know how.
- No HashMap, as we need to do it in O(1) space complexity.
- How can we use the fact that it is sorted in non-decreasing order, to our
advantage?
- If we are at value of 2, and our target is 5. Then we know that most likely our
next value which is hopefully 3, would lead us to that target. But the next value
might be 4, and that could change up the entire equation and situation.
- There will always be exactly one valid solution.
- The array IS SORTED. If your sum with the 2 pointers is too BIG, it should move
to the left. If it is too SMALL it should move to the right, and you will eventually
land up on the one correct solution.
- Naturally r goes down and l goes up. But now we do those 2 natural moves, based on
our specific conditions.
"""