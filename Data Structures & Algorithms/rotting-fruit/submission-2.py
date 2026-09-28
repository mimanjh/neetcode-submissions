class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # go through all values and store rotten fruit in queue
        # while queue exists, spread from that point horizontally and vertically
        # count the number of fresh fruits
        # everytime it rots, reduce it by 1
        # if there are fruits left, return -1, otherwise, return the minutes
        ROWS = len(grid)
        COLS = len(grid[0])
        minutes = 0
        fresh = 0
        queue = collections.deque()
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append([i, j])
        
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (
                        0 <= nr < ROWS and
                        0 <= nc < COLS and
                        grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append([nr, nc])
            minutes += 1

        return minutes if fresh == 0 else -1