class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        sMap = {}
        for s in strs:
            k = len(s) # creating a substring for each char range
            for i in range(k):
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