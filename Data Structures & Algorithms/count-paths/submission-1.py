class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def memo(r, c, rows, cols, cache):
            if r == rows or c == cols:
                return 0
            if cache[r][c] > 0:
                return cache[r][c]
            if r == rows - 1 and c == cols - 1:
                return 1
            
            cache[r][c] = memo(r + 1, c, rows, cols, cache) + memo(r, c + 1, rows, cols, cache)

            return cache[r][c]
        
        grid = [[0] * n for _ in range(m)]
        
        return memo(0, 0, m, n, grid)
            