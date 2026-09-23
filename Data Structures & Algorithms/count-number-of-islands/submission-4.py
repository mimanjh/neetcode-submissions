class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(row, col):
            if (
                row < 0 or
                col < 0 or
                row >= ROWS or
                col >= COLS or
                grid[row][col] == "0"
            ):
                return
            
            grid[row][col] = "0"
            for dr, dc in directions:
                dfs(row + dr, col + dc)
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    dfs(row, col)
                    islands += 1
        
        return islands