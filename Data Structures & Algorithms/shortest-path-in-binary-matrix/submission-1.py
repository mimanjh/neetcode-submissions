class Solution:
    from collections import deque
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # if the grid starts with 1, it fails
        # use queue to pop the last
        # keep track of where we've visited so that it doesn't go the same place again
        # calculate the distance each time the queue goes forward
        # check all 8 directions for possible clear path
        # if the queue reaches the end, return the distance it took there
        # otherwise return -1 to show there's no path

        N = len(grid)
        if grid[0][0] == 1 or grid[N-1][N-1] == 1:
            return -1
        
        visit = set((0, 0))
        queue = deque([(0, 0, 1)])
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        while queue:
            r, c, d = queue.popleft()
            if r == N -1 and c == N - 1:
                return d
            
            for dr, dc in neighbors:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visit and grid[nr][nc] == 0:
                    queue.append((nr, nc, d + 1))
                    visit.add((nr, nc))

        return -1