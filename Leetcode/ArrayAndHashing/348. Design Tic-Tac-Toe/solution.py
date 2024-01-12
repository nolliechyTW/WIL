class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        # Rows, columns and two diagonals
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        # Determine player's mark (1 for player 1 and -1 for player 2)
        mark = 1 if player == 1 else -1

        # Update rows and columns count
        self.rows[row] += mark
        self.cols[col] += mark

        # Update diagonal
        if row == col:
            self.diagonal += mark

        # Update anti-diagonal
        if row + col == self.n - 1:
            self.anti_diagonal += mark

        # Check if the current player wins
        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or \
           abs(self.diagonal) == self.n or abs(self.anti_diagonal) == self.n:
            return player

        # Otherwise, no one wins yet
        return 0

# Example Usage
# ticTacToe = TicTacToe(3)
# print(ticTacToe.move(0, 0, 1))  # return 0 (no one wins)
# print(ticTacToe.move(0, 2, 2))  # return 0 (no one wins)
# print(ticTacToe.move(2, 2, 1))  # return 0 (no one wins)
# print(ticTacToe.move(1, 1, 2))  # return 0 (no one wins)
# print(ticTacToe.move(2, 0, 1))  # return 0 (no one wins)
# print(ticTacToe.move(1, 0, 2))  # return 0 (no one wins)
# print(ticTacToe.move(2, 1, 1))  # return 1 (player 1 wins)
