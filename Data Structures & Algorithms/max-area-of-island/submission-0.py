class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # go through each values in grid
        # if grid[r][c] == 1, run dfs to calculate area
        # in dfs, return the area while making passed island into 0 (water)
        # return max area

        def dfs(r, c):
            # if edges or grid[r][c] == 0, skip
            if r < 0 or r == len(grid) or c < 0 or c == len(grid[0]) or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        
        area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area = max(area, dfs(r, c))

        return area