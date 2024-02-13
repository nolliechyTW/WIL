## 863. All Nodes Distance K in Binary Tree
🔗  Link: [All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Tree, BFS, DFS<br>

=======================================================================================<br>
Given the `root` of a binary tree, the value of a `target` node target, and an integer `k`, return an array of the values of all nodes that have a distance `k` from the target node.

You can return the answer in **any order**.<br>

Example 1:<br>
![img1](image.png)<br>
Input: [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]<br>
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.<br>

Example 2:<br>
Input: root = [1], target = 1, k = 3<br>
Output: []<br>


Constraints:<br>
- The number of nodes in the tree is in the range [1, 500]
- 0 <= Node.val <= 500
- All the values Node.val are unique
- target is the value of one of the nodes in the tree
- 0 <= k <= 1000
=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Are all values in tree unique?
    - all values in the tree are unique
2. Any requirement on time/space complexity?
    - O(N) Time and O(N) Space
3. Can the input tree be Null?
    - No, there will at least be one node


### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1. Graph Representation of a Tree
- First transforms the tree into a graph representation where **each node points to its children and its parent**, effectively making it an undirected graph. This is crucial for allowing **bidirectional traversal**, which is not inherently possible in a tree structure since trees are typically navigated in a top-down manner. This is particularly useful when you need to move both up (towards the parent) and down (towards the children) from any given node

2. Depth-First Search (DFS) for *Graph Building*: 
- The `build_graph` helper function uses DFS to traverse the tree and build the graph representation. DFS is a common technique for exploring all the nodes and edges in a graph or tree, ensuring that each connection (including parent-child and child-parent links) is represented

3. Breadth-First Search (BFS) for *Level Traversal*: 
- Once the graph is built, we use BFS starting from the target node to find all nodes that are k distance away. BFS is employed here because it explores neighbors of all nodes at the current depth before moving on to the nodes at the next depth level, making it ideal for level-by-level traversal to find nodes exactly k steps away

4. Queue for BFS Implementation: 
- The algorithm uses a queue to keep track of nodes to visit and their corresponding distance from the target node. Queues are a fundamental component for implementing BFS, allowing the algorithm to process nodes in a first-in, first-out (FIFO) order

5. Set for Tracking Visited Nodes: 
- A set named `seen` is used to track visited nodes to prevent revisiting and thus avoid infinite loops. This is a common pattern in graph traversal problems to ensure each node is processed exactly once



### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: converting the binary tree into a graph representation and then performing a breadth-first search (BFS) from the target node to find all nodes that are k distance away

1. Graph Representation: 
- It starts by creating a graph (`self.graph`) representation of the tree. **In this graph, each node points to its adjacent nodes (parent, left child, and right child)**. This is achieved through the `build_graph` helper function, which recursively traverses the tree and adds each node's parent and children to the self.graph dictionary. **This dictionary is keyed by nodes, with each key's value being a list of adjacent nodes**

2. Initializing Variables:
- `seen` is a set used to keep track of visited nodes to avoid revisiting them during the BFS
- `an`s is a list to store the values of nodes that are k distance away from the target node

3. BFS Traversal:
- The BFS starts with a queue initialized with the `target` node and a distance of `0`
- The code then enters a loop that continues until the queue is empty.
- It dequeues an element (node and its distance from the target), checks if the distance is equal to `k`, and if so, adds the node's value to the ans list
- It then iterates through all neighbors (parent, left child, right child) of the current node. *For each neighbor not yet visited, it adds the neighbor to seen to mark it as visited and enqueues the neighbor with its distance from the target incremented by 1*

4. Returning Result: 
- Once the BFS is complete, the ans list, which now contains the values of all nodes that are exactly k distance away from the target node, is returned



### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the number nodes in tree.

- Time Complexity: O(N); O(N) for building graph + O(N) for BFS traversal
- Space Complexity: O(N)
    - Graph Storage: The graph stores each node along with its adjacent nodes. Since each edge (parent-child relationship) will be stored twice (once from parent to child and once from child to parent), the space required for the graph is `O(2N)=O(N)`
    - Queue for BFS: In the worst case, the queue used for BFS might need to store a level of the tree. In a balanced binary tree, this would be `O(N/2)` at the last level, which simplifies to O(N)
    - Seen Set: The `seen` set could potentially hold all nodes in the tree if the BFS traverses the entire tree, requiring O(N) space
    - Answer List: In the worst case, particularly when `k` is large enough to encompass many nodes or the entire tree, the answer list could include a significant portion of the nodes. In the worst-case scenario, this could also be O(N), though practically it's expected to be much less unless k is large relative to the tree size.
