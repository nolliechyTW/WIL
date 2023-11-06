## 36. Valid Sudoku

🔗 Link: [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array, Hash<br>

=======================================================================================<br>
Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits `1-9` without repetition.
Each column must contain the digits `1-9` without repetition.
Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

Note:

- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

Example 1:<br>
Input: board = <br>
    [["5","3",".",".","7",".",".",".","."]<br>
    ,["6",".",".","1","9","5",".",".","."]<br>
    ,[".","9","8",".",".",".",".","6","."]<br>
    ,["8",".",".",".","6",".",".",".","3"]<br>
    ,["4",".",".","8",".","3",".",".","1"]<br>
    ,["7",".",".",".","2",".",".",".","6"]<br>
    ,[".","6",".",".",".",".","2","8","."]<br>
    ,[".",".",".","4","1","9",".",".","5"]<br>
    ,[".",".",".",".","8",".",".","7","9"]]<br>
Output: true<br>

Example 2:<br>
Input: board = <br>
    [["8","3",".",".","7",".",".",".","."]<br>
    ,["6",".",".","1","9","5",".",".","."]<br>
    ,[".","9","8",".",".",".",".","6","."]<br>
    ,["8",".",".",".","6",".",".",".","3"]<br>
    ,["4",".",".","8",".","3",".",".","1"]<br>
    ,["7",".",".",".","2",".",".",".","6"]<br>
    ,[".","6",".",".",".",".","2","8","."]<br>
    ,[".",".",".","4","1","9",".",".","5"]<br>
    ,[".",".",".",".","8",".",".","7","9"]]<br>
Output: false<br>
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.<br>

Constraints:<br>
board.length == 9 <br>
board[i].length == 9 <br>
board[i][j] is a digit 1-9 or '.' <br>
=======================================================================================<br>

### UMPIRE Method:

#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Any requirement on time/space complexity?

### Match

> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Storing the elements of the array in a HashMap or a Set<br>
   As we iterate through the array, we can store each number in a Set. If the number is already in the Set, then we can return True. Otherwise we reach the end of the array and return False.

### Plan

> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Create a Set to store number. If the number is already in the Set, then return True. Otherwise we reach the end of the array and return False.

1. Create Set
2. Iterate through numbers
   - If number is already in set return True
   - Else store number in set
3. Return False if we have reached the end of the list without duplicate

### Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review

> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

### Evaluate

> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the number of items in the array.

- Time Complexity: O(N)
- Space Complexity: O(N)
