class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs going through individual values to check if they are 1
        # default value should be when it hits the boundary of sea ("0")
        # go all directions to check if it's 1 or 0
        # every large iteration would result in count += 1
        # return count

        count = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(row, col):
            # default case
            if (
                row < 0 or
                row >= ROWS or
                col < 0 or
                col >= COLS or
                grid[row][col] == "0"
            ):
                return
            
            grid[row][col] = "0"

            for dr, dc in directions:
                dfs(row + dr, col + dc)
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        
        return count
