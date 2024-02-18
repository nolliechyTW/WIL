"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        hashmap = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            current_node = queue.popleft()
            for neighbor in current_node.neighbors:
                if neighbor not in hashmap:
                    # Clone the neighbor and add it to the hashmap
                    hashmap[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                # Add the cloned neighbor to the current node's cloned neighbors list
                hashmap[current_node].neighbors.append(hashmap[neighbor])

        return hashmap[node]
