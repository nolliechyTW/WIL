class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node(0, 0)  # Dummy head
        self.tail = Node(0, 0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        # Always add the new node right after head.
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        # Remove an existing node from the linked list.
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        # Move certain node in between to the head.
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        # Pop the current tail.
        res = self.tail.prev
        self._remove_node(res)
        return res

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1
        # Move the accessed node to the head;
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if not node: 
            newNode = Node(key, value)
            self.cache[key] = newNode
            self._add_node(newNode)
            if len(self.cache) > self.capacity:
                # Pop the tail
                tail = self._pop_tail()
                del self.cache[tail.key]
        else:
            # Update the value.
            node.value = value
            self._move_to_head(node)
