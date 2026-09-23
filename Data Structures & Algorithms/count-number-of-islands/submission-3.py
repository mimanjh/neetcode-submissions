class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs
        # go through each element and update it to 0 and move to adjacent
        # 1s and convert them to 0s as well. If you encounter another 1 
        # afterwards, it should increase the counter

        islands = 0

        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(row, col):
            # default case of hitting each edges and not an island
            if (row < 0 or
                col < 0 or
                row >= ROWS or
                col >= COLS or
                grid[row][col] == "0"):
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