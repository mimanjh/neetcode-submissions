class Solution:
    from collections import deque
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] == 1 or grid[N - 1][N - 1]:
            return -1

        visit = set((0, 0))
        queue = deque([(0, 0, 1)])
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        while queue:
            r, c, length = queue.popleft()
            if r == N - 1 and c == N - 1:
                return length

            for dr, dc in neighbors:
                nRow = r + dr
                nCol = c + dc
                
                if 0 <= nRow < N and 0 <= nCol < N and grid[nRow][nCol] == 0 and (nRow, nCol) not in visit:
                    queue.append((nRow, nCol, length + 1))
                    visit.add((nRow, nCol))
        
        return -1