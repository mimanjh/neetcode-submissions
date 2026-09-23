class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # recursively go through the m x n grid by saving cache of paths that has already been taken
        def cache(r, c, rows, cols, res):
            if r == rows or c == cols:
                return 0
            if res[r][c] > 0:
                return res[r][c]
            if r == rows - 1 and c == cols - 1:
                return 1

            res[r][c] = cache(r + 1, c, rows, cols, res) + cache(r, c + 1, rows, cols, res)

            return res[r][c]
        
        return cache(0, 0, m, n, [[0] * n for _ in range(m)])