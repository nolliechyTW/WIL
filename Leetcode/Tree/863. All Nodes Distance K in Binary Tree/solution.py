# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.graph = defaultdict(list)
        seen ={target} # Set to keep track of visited nodes
        ans = []

        # Helper function to build a graph representation of the tree
        # The graph is represented as a dictionary where the key is a node and the value is a list of its neighbors
        def build_graph(node, parent):
            if not node:
                return
            if parent:
                self.graph[node].append(parent)
            if node.left:
                self.graph[node].append(node.left)
                build_graph(node.left, node)
            if node.right:
                self.graph[node].append(node.right)
                build_graph(node.right, node)

        build_graph(root, None)
        
        queue = deque([(target, 0)]) # BFS queue: node, distance/level from target
        while queue:
            node, distance = queue.popleft()
            if distance == k:
                ans.append(node.val)
            for neighbor in self.graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, distance + 1))
        return ans
        