class Node:
    
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left, self.right = Node(None, None), Node(None, None)
        self.left.next, self.right.prev = self.right, self.left # everything will be added in between these 2 LL pointers

    def get(self, key: int) -> int:
        if key in self.cache: # it has been used so move it to the right pointer (recent)
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val # return the value
        else:
            return -1

    def insert(self, node) -> None:
        # self.right.prev initially pointed to left pointer, our LRU
        # so we constantly keepn adding between the left and right pointer, and this way,
        # the leftmost pointer always keeps track of the LRU
        prev = self.right.prev
        nxt = self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt
    
    def remove(self, node) -> None:
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev # completely stop referencing to the node itself

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


