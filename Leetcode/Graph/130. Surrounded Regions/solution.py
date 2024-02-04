class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        def mark_escape(row, col):
            if 0 <= row < rows and 0 <= col < cols and board[row][col] == 'O':
                board[row][col] = 'E'
                for dr, dc in directions:
                    mark_escape(row + dr, col + dc)

        # Mark the "escaped" cells
        for row in range(rows):
            for col in range(cols):
                if (row in [0, rows-1] or col in [0, cols-1]) and board[row][col] == 'O':
                    mark_escape(row, col)

        # Flip the captured cells ('O'->'X') and the escaped ones ('E'->'O')
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'E':
                    board[row][col] = 'O'