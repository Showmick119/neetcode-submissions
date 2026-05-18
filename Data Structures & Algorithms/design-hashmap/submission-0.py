# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

class MyHashMap:

    def __init__(self):
        self.load_factor = 0.75
        self.capacity = 10
        self.size = 0
        self.array = [(None, None)] * self.capacity

    def put(self, key: int, value: int) -> None:
        if self.size / self.capacity >= self.load_factor:
            self._resize()
        special = False
        specialIdx = 0
        idx = hash(key) % self.capacity
        while self.array[idx][0] is not None and idx < self.capacity:
            # if it's the same key, then update value
            # if different key, then probe
            # if deleted key, then store that index and probe ahead
            # to check there's no duplicate. if no duplicate then
            # put it at the deleted key you stored
            if key == self.array[idx][0]:
                self.array[idx] = (key, value) # updating value when same key
                return # return immediately
            elif self.array[idx][0] == 'DELETED':
                special = True
                specialIdx = idx # store for now, but look ahead and check if there's a duplicate
            else:
                idx = (idx + 1) % self.capacity
        if special:
            # storing at the first DELETED token we run into
            self.array[specialIdx] = (key, value)
        else:
            # storing at the first None spot we run into, if no DEL token found
            self.array[idx] = (key, value)
        self.size += 1

    def get(self, key: int) -> int:
        idx = hash(key) % self.capacity
        while self.array[idx][0] is not None and idx < self.capacity:
            if key == self.array[idx][0]:
                return self.array[idx][1]
            else:
                idx = (idx + 1) % self.capacity
        return -1

    def remove(self, key: int) -> None:
        idx = hash(key) % self.capacity
        while self.array[idx][0] is not None and idx < self.capacity:
            if key == self.array[idx][0]:
                self.array[idx] = ('DELETED', None)
                self.size -= 1
                return
            else:
                idx = (idx + 1) % self.capacity
                # keep probing till we find it
                # if we land on null, that means the element was never added
    
    def _resize(self) -> None:
        temp = self.array
        self.capacity = self.capacity * 2
        self.array = [(None, None)] * self.capacity
        self.size = 0
        for key, value in temp:
            if key == None or key == 'DELETED':
                continue
            else:
                self.put(key, value)

"""
- 
"""