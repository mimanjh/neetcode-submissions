class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def memo(r, c, rows, cols, cache):
            if r == rows or c == cols or obstacleGrid[r][c] == 1:
                return 0
            if cache[r][c] > 0:
                return cache[r][c]
            if r == rows - 1 and c == cols - 1:
                return 1
            
            cache[r][c] = memo(r + 1, c, rows, cols, cache) + memo(r, c + 1, rows, cols, cache)

            return cache[r][c]
        
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        GRID = [[0] * COLS for _ in range(ROWS)]

        return memo(0, 0, ROWS, COLS, GRID)