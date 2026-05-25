class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        longest = max(len(word1), len(word2))
        for i in range(longest):
            if i >= len(word1):
                merged += word2[i:]
                break
            elif i>= len(word2):
                merged += word1[i:]
                break
            merged += word1[i]
            merged += word2[i]
        return merged

"""
- Construct a new string by merging them in alternating order. Start with word1. Take
one character from word1 and then one character from word2.
- If one string is longer than the other, append the remaining characters from the 
longer string to the end of the merged result.
- Only lowercase English letters.
"""