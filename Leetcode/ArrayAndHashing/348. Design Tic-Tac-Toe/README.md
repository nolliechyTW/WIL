## 348. Design Tic-Tac-Toe
🔗  Link: [Design Tic-Tac-Toe](https://leetcode.com/problems/design-tic-tac-toe/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array, Hashmap, Design<br>

=======================================================================================<br>
Assume the following rules are for the tic-tac-toe game on an `n x n` board between two players:<br>

1) A move is guaranteed to be valid and is placed on an empty block.
2) Once a winning condition is reached, no more moves are allowed.
3) A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.

Implement the `TicTacToe` class:<br>
- `TicTacToe(int n)` Initializes the object the size of the board n.
- `int move(int row, int col, int player)` Indicates that the player with id `player` plays at the cell (row, col) of the board. The move is guaranteed to be a valid move, and the two players alternate in making moves. Return
- `0` if there is no winner after the move,
- `1` if player 1 is the winner after the move, or
- `2` if player 2 is the winner after the move.

Example 1:<br>
Input:<br>
["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]<br>
[[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]<br>
Output:<br>
[null, 0, 0, 0, 0, 0, 0, 1]<br>

Explanation:
TicTacToe ticTacToe = new TicTacToe(3);<br>
Assume that player 1 is "X" and player 2 is "O" in the board.<br>
ticTacToe.move(0, 0, 1); // return 0 (no one wins)<br>
|X| | |<br>
| | | |    // Player 1 makes a move at (0, 0).<br>
| | | |<br>

ticTacToe.move(0, 2, 2); // return 0 (no one wins)<br>
|X| |O|<br>
| | | |    // Player 2 makes a move at (0, 2).<br>
| | | |<br>

ticTacToe.move(2, 2, 1); // return 0 (no one wins)<br>
|X| |O|<br>
| | | |    // Player 1 makes a move at (2, 2).<br>
| | |X|<br>

ticTacToe.move(1, 1, 2); // return 0 (no one wins)<br>
|X| |O|<br>
| |O| |    // Player 2 makes a move at (1, 1).<br>
| | |X|<br>

ticTacToe.move(2, 0, 1); // return 0 (no one wins)<br>
|X| |O|<br>
| |O| |    // Player 1 makes a move at (2, 0).<br>
|X| |X|<br>

ticTacToe.move(1, 0, 2); // return 0 (no one wins)<br>
|X| |O|<br>
|O|O| |    // Player 2 makes a move at (1, 0).<br>
|X| |X|<br>

ticTacToe.move(2, 1, 1); // return 1 (player 1 wins)<br>
|X| |O|<br>
|O|O| |    // Player 1 makes a move at (2, 1).<br>
|X|X|X|<br>



Constraints:<br>
- 2 <= n <= 100
- player is 1 or 2.
- 0 <= row, col < n
- (row, col) are unique for each different call to move
- At most n^2 calls will be made to move

=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Are there any specific rules for the game play, other than the standard Tic-Tac-Toe rules? For example, are players allowed to skip their turn, or are turns strictly alternating?
2. Since the move is guaranteed to be valid, am I correct in assuming that the input to the move function will always be within bounds and the cell will always be empty? Or should the function handle cases where a move is out of bounds or on an already occupied cell?
3. Any requirement on time/space complexity? 
    - try to come up with a time complexity of O(1) for each move



### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1. Arrays/Matrix
The core of this problem revolves around manipulating and checking the states of elements in a 2D array or matrix, as a Tic-Tac-Toe board can be effectively represented as a 2D grid. Each cell in the grid can hold a value indicating the state (empty, player 1, player 2)

2. Pattern: Design/Class Structure: 
The problem is approached using Object-Oriented Programming (OOP), encapsulating the Tic-Tac-Toe game logic within a class. This design pattern is useful for maintaining the state of the game and the logic associated with each move

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

- General Idea: the main idea is to efficiently check whether a player has won the game after each move, without having to check the entire board state. This is achieved through the use of counters for rows, columns, and diagonals.

1) Initialization (`__init__` method):
    - The constructor initializes the game board size (`n`) and sets up four counters: `rows`, `cols`, `diagonal`, and `anti_diagonal`. Each counter (except the diagonals, which are single integers) is a list of length `n` initialized to `0`. These counters will track the sum of marks for each row, column, and the two diagonals
2) Making a Move (`move` method):
    - The move method allows a player to place a mark on the board. The mark is represented by `1` for player 1 and `-1` for player 2. This method updates the counters based on the player's move
    - Updating Counters: When a player makes a move at (row, col), the method updates the corresponding row and column counters by adding the player's mark (1 or -1). If the move is on the main diagonal (row == col), the main diagonal counter is updated. Similarly, if the move is on the anti-diagonal (`row + col == n - 1`), the anti-diagonal counter is updated.
    - Checking for a Win: After updating the counters, the method checks if any of the counters equal `n` or `-n`. A value of n indicates that player 1 has filled an entire row, column, or diagonal with their marks, whereas -n indicates the same for player 2. If such a condition is met, the current player wins, and the method returns the player's number (1 or 2).
    - If no win condition is met, the method returns `0`, indicating that the game continues without a winner yet.



### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N is the size of the board. 

- Time Complexity: O(1) per `move` operation
- Space Complexity: O(n)