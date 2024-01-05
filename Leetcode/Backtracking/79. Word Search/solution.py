class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        # Check if the word is longer than the total number of cells in the grid
        if rows * cols < len(word):
            return False

        def dfs(i, j, k):
            # Boundary check and character match check
            if 0 <= i < rows and 0 <= j < cols and board[i][j] == word[k]:
                # Check if we have found the last character of the word
                if k == len(word) - 1:
                    return True

                # Temporarily mark the cell as visited
                temp, board[i][j] = board[i][j], '*'

                # Continue the search in adjacent cells
                found = False
                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    if dfs(i+di, j+dj, k+1):
                        found = True
                        break

                # Backtrack by restoring the cell's original value
                board[i][j] = temp

                return found
            return False

        # Start DFS from each cell
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False

# Example usage
solution = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(solution.exist(board, word))  # Output: True
