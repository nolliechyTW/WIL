## 200. Number of Islands
🔗  Link: [Number of Islands](https://leetcode.com/problems/number-of-islands/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Matrix, DFS, BFS<br>

=======================================================================================<br>
Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.<br>

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.<br>

Example 1:<br>
Input: grid = [<br>
  ["1","1","1","1","0"],<br>
  ["1","1","0","1","0"],<br>
  ["1","1","0","0","0"],<br>
  ["0","0","0","0","0"]<br>
]<br>
Output: 1<br>

Example 2:<br>
Input: grid = [<br>
  ["1","1","0","0","0"],<br>
  ["1","1","0","0","0"],<br>
  ["0","0","1","0","0"],<br>
  ["0","0","0","1","1"]<br>
]<br>
Output: 3<br>


Constraints:<br>
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- `grid[i][j]` is '0' or '1'.

=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the input grid be empty?
    - No
2. Any requirement on time/space complexity?
    - O(m * n) in time and O(1) in space 
3. Can islands have irregular shapes, or are they always rectangular?
    - Yes
4. Do diagonal connections between lands count towards forming an island?
    - No

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Depth-First Search (DFS)
    1) Traversal: Iterate over each cell in the grid. When a land cell ('1') is found, increment the island count and then traverse its neighboring land cells to mark the entire island

    2) Marking Visited Cells: To avoid counting the same land twice, we can mark the visited land cells by either changing their value to '0' (water) or using a separate visited structure

    3) Recursion: Implement DFS recursively. When a land cell is found, call DFS for its four adjacent (up, down, left, right) cells

    4) Edge Handling: Ensure that the DFS does not go out of bounds of the grid and only processes land cells

    5) Complexity: Time complexity would be O(mn) where m is the number of rows and n is the number of columns, since each cell is processed once. The space complexity depends on the recursion depth, which can be up to O(mn) in the worst case (completely filled with land)

2. Breadth-First Search (BFS)
    1) Queue-based Implementation: Use a queue to implement BFS. When a land cell is found, add it to the queue and process its neighbors iteratively.

    2) Marking and Processing: Similar to DFS, mark cells as visited. Process cells in the queue and add their unvisited land neighbors to the queue.

    3) Iterative Approach: BFS is naturally iterative, which avoids the potential stack overflow issue of DFS in large grids.

    4) Complexity: Time complexity remains O(m*n) as all cells are processed once. The space complexity is O(min(m,n)) in the worst case, as in the worst case, the queue will have all cells from the largest row or column.

In most standard cases for this problem, **DFS would be the preferred choice** due to its *straightforward implementation and efficient handling of the typical sizes and shapes* of islands in the grid. However, if you're working with *extremely large grids or have specific constraints that favor an iterative approach*, then **BFS** would be the better option.


### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: uses a Depth-First Search (DFS) approach to explore the grid and identify the islands; we can either save the island we have visited or mark the island by changing its value

1) Initialize Count and Directions: We start by initializing a counter `ans` to `0`, which will hold our total number of islands. We also set up a `direction` array to easily check adjacent cells (up, down, left, right)

2) Iterate Over the Grid: We loop through each cell in the `grid`. For each cell, we check if it is land (`'1'`). If it's water (`'0'`), we do nothing and continue to the next cell.

3) Depth-First Search (DFS): When we encounter a land cell (`'1'`), we increment our `ans` counter because we've found a new island. We then perform a DFS starting from this cell to mark the entire island:

    - We **change the current land cell to '0' to mark it as visited**
    - We recursively call DFS on all adjacent land cells (up, down, left, right)

4) Marking Island Territory: The DFS will continue to spread from each land cell to its adjacent land cells, marking each as visited (`'0'`). This process ensures that we count all connected `'1'`s as a single island.

5) Complete the Search: Once DFS is complete for an island, the search continues from the next unvisited land cell in the grid. Each new unvisited land cell starts a new DFS and potentially identifies a new island.

6) Return the Count: After we've processed the entire grid, the value of `ans` will be the total number of distinct islands.



### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

If the grid has M rows and N columns, there are a total of M * N cells.

- Time Complexity: O(M*N)
- Space Complexity: O(M*N); The main space consumption in the algorithm comes from the recursion stack used in DFS. In the worst case (when the grid is entirely filled with land), the maximum depth of the recursive call stack could be m * n, in scenarios where DFS traverses the entire grid.