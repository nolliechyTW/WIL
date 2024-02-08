class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        # Initialize sets to keep track of visited cells
        rows, cols = len(matrix), len(matrix[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        pacific_reachable = set()
        atlantic_reachable = set()
        
        def dfs(row, col, reachable):
            # This cell is reachable, so mark it
            reachable.add((row, col))
            for (x, y) in directions: # Check all 4 directions
                new_row, new_col = row + x, col + y
                # Check if the new cell is within bounds
                if not (0 <= new_row < rows and 0 <= new_col < cols):
                    continue
                # Check that the new cell hasn't already been visited
                if (new_row, new_col) in reachable:
                    continue
                # Check that the new cell has a higher or equal height,
                # So that water can flow from the new cell to the old cell
                if matrix[new_row][new_col] < matrix[row][col]:
                    continue
                # If we've gotten this far, that means the new cell is reachable
                dfs(new_row, new_col, reachable)
        
        # Loop through each cell adjacent to the oceans and start a DFS
        for i in range(rows): # Vertical Edges
            dfs(i, 0, pacific_reachable) # Left edge
            dfs(i, cols - 1, atlantic_reachable) # Right edge
        for i in range(cols): # Horizontal Edges
            dfs(0, i, pacific_reachable) # Top edge
            dfs(rows - 1, i, atlantic_reachable) # Bottom edge
        
        # Find all cells that can reach both oceans, and convert to list
        return list(pacific_reachable.intersection(atlantic_reachable))