# https://leetcode.com/problems/lru-cache/
class Node:

    def __init__(self, key: int, value: int):
        self.key, self.value = key, value
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> node

        # dummy nodes to create linked list
        # right = lru, left = most recently used
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def _remove_node(self, node: Node):
        prev_node, next_node = node.prev, node.next
        prev_node.next, next_node.prev = next_node, prev_node

    def _insert_node(self, node: Node):
        prev_node, next_node = self.right.prev, self.right
        prev_node.next, next_node.prev = node, node
        node.next, node.prev = next_node, prev_node

    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove_node(self.cache[key])
            self._insert_node(self.cache[key])

            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove_node(self.cache[key])

        self.cache[key] = Node(key, value)
        self._insert_node(self.cache[key])

        if len(self.cache) > self.capacity:
            lru_node = self.left.next
            self._remove_node(lru_node)

            del self.cache[lru_node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
assert lru.get(1) == 1
lru.put(3, 3)
assert lru.get(2) == -1
lru.put(4, 4)
assert lru.get(1) == -1
assert lru.get(3) == 3
assert lru.get(4) == 4
