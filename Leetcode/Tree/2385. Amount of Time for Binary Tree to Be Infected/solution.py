# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.graph = defaultdict(list)
        infected = set() # Use set for quick lookup
        minutes = -1 # Initialize to -1 to correct off-by-one error

        # Build graph with node values as keys
        def build_graph(node, parent):
            if not node:
                return
            if parent:
                self.graph[node.val].append(parent.val)
            if node.left:
                self.graph[node.val].append(node.left.val)
                build_graph(node.left, node)
            if node.right:
                self.graph[node.val].append(node.right.val)
                build_graph(node.right, node)
        
        build_graph(root, None)

        # Initialize queue with the start node value
        queue = deque([start])
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                current = queue.popleft()
                infected.add(current)
                # Iterate through neighbors of the current node
                for neighbor in self.graph[current]:
                    if neighbor not in infected:
                        infected.add(neighbor)
                        queue.append(neighbor)
            minutes += 1

        return minutes