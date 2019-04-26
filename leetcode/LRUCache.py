class LRUCache:

    def __init__(self, capacity: int):
        assert (capacity > 0)
        self.map = {}
        self.head = None
        self.tail = None
        self.length = 0
        self.capacity = capacity

    def push_node_to_head(self, node):
        prev = node.prev
        next_ = node.next

        if next_:
            next_.prev = prev
        else:
            self.tail = prev

        if prev:
            prev.next = next_

        node.next, node.prev = self.head, None
        self.head = node

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.push_node_to_head(node)
            self.print()
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            return

        if self.length == 0:
            self.length += 1
            new_node = Node(key, value)
            self.head = new_node
            self.tail = new_node
            self.map[key] = self.head
            return

        print("self.head.prev: {}".format(self.head.val))
        head_ = self.head
        self.head = Node(key, value, head_)
        head_.prev = self.head

        self.map[key] = self.head
        self.length += 1

        if self.length > self.capacity:
            tail_ = self.tail
            print(tail_.key)
            print(tail_.prev.val)
            tail_.prev.next = None

            del self.map[tail_.key]
            self.length -= 1

            self.tail = tail_

    def print(self):
        node = self.head
        while node:
            print("({}, {}) ".format(node.key, node.val), end=", ")
            node = node.next


class Node:

    def __init__(self, key, val, next_=None):
        self.prev = None
        self.next = next_
        self.key = key
        self.val = val


cache = LRUCache(2)
print(cache.put(1, 1))      # return None
print(cache.put(2, 2))      # return None
print(cache.get(1))         # returns 1
print(cache.put(3, 3))     # evicts key 2
#print(cache.get(2))         # returns -1 (not found)
#print(cache.put(4, 4))     # evicts key 1
#print(cache.get(1))         # returns -1 (not found)
#print(cache.get(3))         # returns 3
#print(cache.get(4))         # returns 4
