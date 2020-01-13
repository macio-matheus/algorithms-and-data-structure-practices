class QNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return f"{self.key}, {self.value}"


class LRUCache(object):
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("capacity > 0")
        self.hash_map = {}

        # No explicit doubly linked queue here (you may create one yourself)
        self.head = None
        self.end = None
        self.capacity = capacity
        self.current_size = 0

    def get(self, key):

        if key not in self.hash_map:
            return -1

        node = self.hash_map[key]

        # small optimization (1): just return the value if we are already looking at head
        if self.head == node:
            return node.value
        self._remove(node)
        self._set_head(node)
        print(f"Returned value: {node.value}")
        return node.value

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.hash_map:
            node = self.hash_map[key]
            node.value = value

            # small optimization (2): update pointers only if this is not head; otherwise return
            if self.head != node:
                self._remove(node)
                self._set_head(node)
        else:
            new_node = QNode(key, value)
            if self.current_size == self.capacity:
                del self.hash_map[self.end.key]
                self._remove(self.end)
            self._set_head(new_node)
            self.hash_map[key] = new_node

    def _set_head(self, node):
        if not self.head:
            self.head = node
            self.end = node
        else:
            node.prev = self.head
            self.head.next = node
            self.head = node
        self.current_size += 1

    def _remove(self, node):
        if not self.head:
            return

        # removing the node from somewhere in the middle; update pointers
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        # head = end = node
        if not node.next and not node.prev:
            self.head = None
            self.end = None

        # if the node we are removing is the one at the end, update the new end
        # also not completely necessary but set the new end's previous to be NULL
        if self.end == node:
            self.end = node.next
            self.end.prev = None
        self.current_size -= 1
        return node

    def print_elements(self):
        n = self.head
        print(f"[head = {self.head}, end = {self.end}]")
        while n:
            print(f"{n}")
            n = n.prev


if __name__ == '__main__':
    cache_lru = LRUCache(10)
    cache_lru.set(1, 100)
    cache_lru.set(2, 200)
    cache_lru.set(3, 300)
    cache_lru.print_elements()
    cache_lru.get(2)
    cache_lru.get(1)
    cache_lru.print_elements()
