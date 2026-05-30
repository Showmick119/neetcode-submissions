class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        count = 0
        while l <= r:
            if l == r:
                count += 1
                l += 1
            elif people[l] + people[r] > limit:
                count += 1
                l += 1
            elif people[l] + people[r] <= limit:
                count += 1
                l += 1
                r -= 1
        return count

"""
- You are given an array called people, where people[i] is the weight of the ith
person, and an infinite number of boats where each boat can carry a maximum weight of
limit.
- Each boat can carry at most two people at the same time, given that their sum is
less than or equal to limit.
- Return the minimum number of boats to carry every given person.
- A boat can carry at most 2 people, but can also carry 1 person.
- There are an infinite number of boats. So how many do we need to carry all listed
people?
- Once a person has been picked up by a boat. He CANNOT be picked up again.
- We can assume, each element is less than the limit. So every person can get on a
1 seater boat.
"""