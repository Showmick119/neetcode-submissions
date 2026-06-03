class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0
        l = 0
        r = len(people) - 1
        people.sort()
        while l <= r:
            if people[l] + people[r] > limit:
                r -= 1
            else:
                l += 1
                r -= 1
            count += 1
        return count

"""
- you prioritize filling up the heavier person first, as they are less likely to be able
to make a good combo with any other person. HOWEVER, the lighter person has a probability
of making a good combo with another person, so you keep them around for more combos and tests.
- can always carry 1 person, and carry at most 2 people.
"""