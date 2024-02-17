# UPDATE: Feb 16, 2024
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def markT(row, col):
            if board[row][col] != 'O':
                return
            board[row][col] = 'T'  # Mark as temporary
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    markT(new_row, new_col)

        # Mark 'O's on the border and connected to the border as 'T'
        for r in range(rows):
            markT(r, 0)
            markT(r, cols - 1)
        for c in range(cols):
            markT(0, c)
            markT(rows - 1, c)

        # Flip all 'O's to 'X's and then flip 'T's back to 'O's
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'


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
            if 0 <= row < rows and 0 <= col < cols and board[row][col] == 'O': # key
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