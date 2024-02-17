class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def copyRandomList(head):
    # Dictionary to hold old node to new node mapping
    node_map = {}

    # Copy all the nodes
    current = head
    while current:
        node_map[current] = Node(current.val)
        current = current.next

    # Assign next and random pointers
    current = head
    while current:
        if current.next:
            node_map[current].next = node_map[current.next]
        if current.random:
            node_map[current].random = node_map[current.random]
        current = current.next

    return node_map[head]
