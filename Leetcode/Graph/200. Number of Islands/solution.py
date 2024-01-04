from collections import deque

# BFS Iterative
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # bfs iterative
        rows = len(grid)
        cols = len(grid[0])
        ans = 0 
        visited = set()
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == '1' and (x, y) not in visited:
                    ans += 1
                    queue = deque([(x, y)])
                    while queue:
                        x, y = queue.popleft()
                        visited.add((x,y))
                        for dx, dy in direction:
                            newx = x + dx
                            newy = y + dy
                            if newx >= 0 and newy >= 0 and newx < rows and newy < cols and (newx, newy) not in visited and grid[newx][newy] == '1':
                                queue.append((newx, newy))        
        
        return ans

# DFS Recursive
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans = 0 
        visited = set()
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x, y):
            visited.add((x, y))
            for dx, dy in direction:
                newx = x + dx
                newy = y + dy
                if newx >= 0 and newy >= 0 and newx < rows and newy < cols and (newx, newy) not in visited and grid[newx][newy] == '1':
                    dfs(newx, newy)

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == '1' and (x, y) not in visited:
                    ans += 1
                    dfs(x, y)
        
        return ans
    
# DFS Improved Recursive
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        ans = 0
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x, y):
            """Perform DFS to mark all parts of the current island."""
            grid[x][y] = '0'  # Mark as visited
            for dx, dy in direction:
                newx, newy = x + dx, y + dy
                if 0 <= newx < rows and 0 <= newy < cols and grid[newx][newy] == '1':
                    dfs(newx, newy)

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == '1':
                    ans += 1
                    dfs(x, y)

        return ans
