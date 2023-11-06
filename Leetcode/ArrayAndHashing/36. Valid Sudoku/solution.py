from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """O(1) in time, O(1) in space"""
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set) # key = (r/3, c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] ==".":
                    continue
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3, c//3)]):
                    return False
                else:
                    rows[r].add(board[r][c]) # {row number: value}
                    cols[c].add(board[r][c]) # {col number: value}
                    squares[(r//3, c//3)].add(board[r][c]) # {[rowblock, colblock]: value}
        return True
