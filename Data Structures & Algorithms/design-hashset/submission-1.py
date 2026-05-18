# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

class MyHashSet:

    def __init__(self):
        self.load_factor = 0.75
        self.capacity = 10 # how much it can store
        self.size = 0 # how much it is actually storing
        self.array = [None] * self.capacity
        # If you initialize with 0, that can be misleading, as
        # user may want to add 0 as an entry. None is a better
        # starting point.

    def add(self, key: int) -> None:
        if (self.size / self.capacity) > self.load_factor:
            self._resize()
        index = hash(key) % self.capacity
        while self.array[index] is not None and index < self.capacity:
            if key == self.array[index]:
                return
                # we don't want to add duplicates
            else:
                index = (index + 1) % self.capacity
        self.array[index] = key

    def remove(self, key: int) -> None:
        index = hash(key) % self.capacity
        while self.array[index] is not None and index < self.capacity:
            if key == self.array[index]:
                self.array[index] = 'DELETED'
                return
            else:
                index = (index + 1) % self.capacity
        return
        # If you run into None, then that means the key was never
        # added.

    def contains(self, key: int) -> bool:
        index = hash(key) % self.capacity
        while self.array[index] is not None and index < self.capacity:
            if key == self.array[index]:
                return True
            else:
                index = (index + 1) % self.capacity
        return False

    def _resize(self) -> None:
        temp = self.array
        self.capacity = self.capacity * 2
        self.array = [0] * self.capacity
        for key in temp:
            # gotta rehash everything
            self.add(key)
        return

"""
- HashSet can be created with both a LinkedList, and also an array.
- Use the key to calculate an index in the array/list.
- There's capacity, and then there's also size.
- '%' always yields a non-negative value.
- Generally there is a load factor, which when exceeded, means you
have to resize the backing array.
- There's external chaining, but there's also open-addressing (linear
& quadratic probing).
- self refers to the current object instance, hence you use it when
calling methods for the current instance in the class code.
- HashSet does not store duplicates. So if you see the exact same
element already exists, stop probing, as we don't want to add
duplicates.
"""