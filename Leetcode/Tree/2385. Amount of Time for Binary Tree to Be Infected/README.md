## 2385. Amount of Time for Binary Tree to Be Infected
🔗  Link: [Amount of Time for Binary Tree to Be Infected](https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Tree, BFS, DFS<br>

=======================================================================================<br>
You are given the `root` of a binary tree with unique values, and an integer `start`. At minute `0`, an infection starts from the node with value `start`.

Each minute, a node becomes infected if:
- The node is currently uninfected.
- The node is adjacent to an infected node.
Return the number of minutes needed for the entire tree to be infected.

<br>

Example 1:<br>
![img](image.png)<br>
Input: root = [1,5,3,null,4,10,6,9,2], start = 3
Output: 4<br>
Explanation: The following nodes are infected during:
- Minute 0: Node 3
- Minute 1: Nodes 1, 10 and 6
- Minute 2: Node 5
- Minute 3: Node 4
- Minute 4: Nodes 9 and 2<br>
It takes 4 minutes for the whole tree to be infected so we return 4.<br>

Example 2:<br>
Input: root = [1], start = 1<br>
Output: 0<br>
Explanation: At minute 0, the only node in the tree is infected so we return 0.<br>



Constraints:<br>
- The number of nodes in the tree is in the range [1, 10^5].
- 1 <= node.val <= 10^5
- Each node has a unique value.
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
4. Will the `start` integer always correspond to a value present in the tree?
    - A node with a value of start exists in the tree.



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
- A set named `infected` is used to track visited nodes to prevent revisiting and thus avoid infinite loops. This is a common pattern in graph traversal problems to ensure each node is processed exactly once



### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: model the infection spread through a binary tree by converting the tree into a graph for easy traversal, employing a BFS strategy to simulate the infection spread minute by minute, and accurately counting the time until the entire tree is infected.



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

