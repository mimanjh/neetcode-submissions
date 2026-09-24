class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        islands = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(row: int, col: int):
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