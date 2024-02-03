## 994. Rotting Oranges
🔗  Link: [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Matrix, DFS, BFS<br>

=======================================================================================<br>
You are given an `m x n` grid where each cell can have one of three values:

- `0` representing an empty cell,
- `1` representing a fresh orange, or
- `2` representing a rotten orange

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return `-1`.<br>

Example 1:<br>
![Alt text](image.png)<br>
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]<br>
Output: 4<br>

Example 2:<br>
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]<br>
Output: -1<br>
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.<br>

Example 3:
Input: grid = [[0,2]]<br>
Output: 0<br>
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.<br>

Constraints:<br>
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 10
- `grid[i][j]` is `0` or `1` or `2`

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
5. What is a possible edge case?
    - That there is no fresh, there is no rotten

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Depth-First Search (DFS)
    1) Traversal: Iterate over each cell in the grid. When a land cell ('1') is found, increment the island count and then traverse its neighboring land cells to mark the entire island

    2) Marking Visited Cells: To avoid counting the same land twice, we can mark the visited land cells by either changing their value to '0' (water) or using a separate visited structure

    3) Recursion: Implement DFS recursively. When a land cell is found, call DFS for its four adjacent (up, down, left, right) cells

    4) Edge Handling: Ensure that the DFS does not go out of bounds of the grid and only processes land cells

    5) Complexity: Time complexity would be O(mn) where m is the number of rows and n is the number of columns, since each cell is processed once. The space complexity depends on the recursion depth, which can be up to O(mn) in the worst case (completely filled with land)

2. Breadth-First Search (BFS)
    - TODO


### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: 


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