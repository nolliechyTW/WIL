class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes = 0
        fresh = 0
        rotten = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten.append((i, j))

        while rotten and fresh:
            # update the number of minutes passed
            minutes += 1  # update the minutes by 1 for each level of BFS traversal

            # process rotten oranges on the current level
            for _ in range(len(rotten)):
                row, col = rotten.popleft()
                for x, y in directions:
                    new_row, new_col = row + x, col + y
                    # Corrected boundary checks here
                    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2  # set fresh orange to rotten
                        fresh -= 1
                        rotten.append((new_row, new_col))

        return minutes if fresh == 0 else -1
