# DFS Recursive solution
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        result = 0 
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(row, col, count):
            # mark as visited
            grid[row][col] = 0
            count += 1
            
            for x, y in directions:
                new_x = row + x
                new_y = col + y

                if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == 1:
                    count = dfs(new_x, new_y, count)
            return count


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    # Since count is reset to 0 for each new island, we pass it as an initial value
                    size = dfs(row, col, 0)
                    result = max(result, size)

        return result