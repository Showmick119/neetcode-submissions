class FreqStack:

    def __init__(self):
        self.frequency = {}
        self.value = {}
        self.maxFreq = 0

    def push(self, val: int) -> None:
        if val in self.value:
            self.value[val] += 1
        else:
            self.value[val] = 1
        
        freq = self.value[val] # make sure to update this always, such that it's in the
        # correct frequency group
        if freq > self.maxFreq:
            self.maxFreq = freq
        
        if freq in self.frequency:
            self.frequency[freq].append(val) # appending to the individual stack of each
            # frequency group
        else:
            self.frequency[freq] = [val]

    def pop(self) -> int:
        # keep decrementing while until you reach the correct group
        if len(self.frequency[self.maxFreq]) != 0:
            out = self.frequency[self.maxFreq].pop()
            self.value[out] -= 1 # update the frequencies to the correct amount
            return out
        else:
            while len(self.frequency[self.maxFreq]) == 0:
                self.maxFreq -= 1
            out = self.frequency[self.maxFreq].pop()
            self.value[out] -= 1 # update the frequencies to the correct amount
            return out

"""
- how do you deal with the times when the frequency of an element increases? you have to pop
it from the previous frequency group and add it to the new one.
- keep two dictionaries, it won't affect your space complexity much. but it will give you a
way of keeping track of frequency
"""