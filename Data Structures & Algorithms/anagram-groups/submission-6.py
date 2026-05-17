class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            newS = "".join(sorted(s))
            if newS in groups:
                groups[newS].append(s)
            else:
                groups[newS] = [s]
        output = []
        for vals in groups.values():
            output.append(vals)
        return output

"""
- First process each one and put it as a key in the dict
- Each key will store a value, which is a list of the
unprocessed strings
- Put all these lists into a bigger list, and then output
that bigger list
"""