class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        sMap = {}
        for s in strs:
            k = len(s) # creating a substring for each char range
            for i in range(k + 1):
                curr = s[0:i]
                if curr not in sMap:
                    sMap[curr] = 1
                else:
                    sMap[curr] += 1
        longest = ""
        longestLen = 0
        for key, value in sMap.items():
            if value != n:
                continue
            if len(key) > longestLen:
                longestLen = len(key)
                longest = key
        if len(longest) > 0:
            return longest
        else:
            return ""

"""
- Arrays and Hashing go hand in hand.
- Keep in mind that no time-complexity has been mentioned, so we
can freestyle.
- Have a HashMap where the key is the substring, and the value is
the quantity of times it showed up.
- For it to be a proper common prefix, it has to show up n-times,
as there's n elements in our strs list.
- In the end, just take the largest key, which showed up n-times.
- O(n * k), where n is the number of strs and k is the average
character count (length) of these strs.
"""

"""
Mistakes:
- range(k) outputs a list of numbers from 0 to k-1.
- Slicing Strings in Python is exclusive. str[0:3] actually only
includes indexes 0, 1 and 2 of the str.
- So in the edge case when we have a single character string, our
variable k equals 1. and then range(k) outputs 0 to k-1, so 0 to 0.
- And slicing doesn't include final index. So "a"[0:0] just gives
an empty string.
- range(k + 1) would output list of numbers from 0 to ((k + 1) - 1)
- then slicing, str[0:k] would exclude kth index, since slicing is
exclusive of the end index. 
- and str doesn't have a kth index, since strings are 0-indexed, 
its indexes would go from 0 to k - 1. so this works in our favor.
"""