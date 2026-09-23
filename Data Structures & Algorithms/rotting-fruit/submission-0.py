class Solution:
    from collections import deque
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs
        # need to find the rotten fruits first and start from there
        # keep track of boundaries
        # store all rotten fruits in queue and pop until empty
        # update current fruit to rotten
        # once it's finished, check if there are any fresh fruits left in the grid
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i, j))
        minutes = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
            if queue:
                minutes += 1
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1

        return minutes