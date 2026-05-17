class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for s in strs:
            # ss = ''.join(sorted(s))
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ss = tuple(count)
            # HashMap after sorting done
            if ss not in mp:
                mp[ss] = [s]
            else:
                mp[ss].append(s)
        output = []
        for key, value in mp.items():
            output.append(value)
        return output

"""
- HashMap Key: sorted string characters
- HashMap Value: actual strings 
- Since recommended time complexity is O(m * n), we cannot just
spam the sort() method.
- So let's first do the simple implementation with sort(), and then
bring in the sorting logic which will cut out the nlogn complexity.
"""

"""
Mistakes:
- To get a String after sorting. You don't do:
s = sorted(s) ## this will give a list
- Do this instead:
s = ''.join(sorted(s))
- The line above will join all elements of the list with an empty
seperator, meaning there won't be any space between the joined
elements.
"""

"""
New Approach for O(m * n) time-complexity:
- Firstly, for each String, create a tuple of 26 entries. Each
entry from index 0-25 represents lowercase characters 'a' to 'z'.
- Each tuple represents a specific String through character
frequency.
- Same tuples (character frequencies), would map to the same key
in the dictionary.
"""