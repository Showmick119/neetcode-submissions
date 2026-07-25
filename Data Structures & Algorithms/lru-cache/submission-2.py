class ListNode:

    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = ListNode() # Least Recently Used, updated when using put()
        self.right = ListNode() # Most Recently Used, updated when using get() and put()
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            output = self.cache[key].value
            self.remove(key) # remove from wherever it currently is
            self.insert(key) # bring it to the absolute front (most recently used)
            return output
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(key)
        self.cache[key] = ListNode(key, value)
        self.insert(key)
        if len(self.cache) > self.capacity:
            # remove the least recently used cache from the left pointer
            lru = self.left.next
            self.remove(lru.key)
            del self.cache[lru.key]
    
    def insert(self, key: int) -> None: # Inserting with the right pointer
        node = self.cache[key]
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

    def remove(self, key: int) -> None:
        node = self.cache[key]
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

"""
- 
"""