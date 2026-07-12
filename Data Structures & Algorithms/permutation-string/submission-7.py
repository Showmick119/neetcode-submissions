class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Freq = [0] * 26
        for char in s1:
            idx = ord('a') - ord(char)
            s1Freq[idx] += 1
        
        from collections import deque
        window = deque()
        l = 0
        windowFreq = [0] * 26
        for i in range(len(s2)):
            char = s2[i]
            idx = ord('a') - ord(char)
            windowFreq[idx] += 1
            window.append(char)
            if len(window) == len(s1):
                if windowFreq == s1Freq:
                    return True
                else:
                    window.popleft()
                    char = s2[l]
                    idx = ord('a') - ord(char)
                    windowFreq[idx] -= 1
                    l += 1
        return False

"""
- can't use hashmaps as it requires o(1) space
- use lists to compare the character frequencies of the substrings of s2 and the string of
s1
- only lowercase letters
- we don't need freq count for the 2nd string itself
- we only need the freq count for the window that goes over the 2nd string
"""