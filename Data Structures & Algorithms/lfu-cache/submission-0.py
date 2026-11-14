class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def append(self, node: Node):
        prev = self.tail.prev

        prev.next = node
        node.prev = prev

        node.next = self.tail
        self.tail.prev = node

        self.size += 1

    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def pop_lru(self) -> Node:
        node = self.head.next
        self.remove(node)
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0

        self.nodes = {}   # key -> Node
        self.groups = {}  # frequency -> DLL

    def _touch(self, node: Node):
        f = node.freq
        self.groups[f].remove(node)

        if f == self.min_freq and self.groups[f].size == 0:
            self.min_freq += 1

        node.freq += 1

        if node.freq not in self.groups:
            self.groups[node.freq] = DLL()

        self.groups[node.freq].append(node)

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1

        node = self.nodes[key]
        self._touch(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.nodes:
            node = self.nodes[key]
            node.value = value
            self._touch(node)
            return

        if len(self.nodes) == self.capacity:
            lru = self.groups[self.min_freq].pop_lru()
            del self.nodes[lru.key]

        node = Node(key, value)
        self.nodes[key] = node

        if 1 not in self.groups:
            self.groups[1] = DLL()

        self.groups[1].append(node)
        self.min_freq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)