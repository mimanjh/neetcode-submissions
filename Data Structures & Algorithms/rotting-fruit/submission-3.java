class Solution {
    public int orangesRotting(int[][] grid) {
        // bfs
        // go through the list and fill up location of rotten fruit
        // while queue exists, for all values in the array,
        // set other oranges that are fresh in its four directions as rotten
        // add those to the queue
        // once you come out of the for loop, that's 1 second, so increment by one second
        // return the total second
        int timer = 0;
        int freshCount = 0;
        Queue<int[]> queue = new LinkedList<>();
        final int ROWS = grid.length;
        final int COLS = grid[0].length;
        final int[][] directions = {
            {1, 0},
            {-1, 0},
            {0, 1},
            {0, -1}
        };

        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j < COLS; j++) {
                if (grid[i][j] == 2) {
                    queue.offer(new int[]{i, j});
                }
                else if (grid[i][j] == 1) {
                    freshCount++;
                }
            }
        }

        while (!queue.isEmpty() && freshCount > 0) {
            int queueSize = queue.size();

            for (int i = 0; i < queueSize; i++) {
                int[] rotten = queue.poll();

                int r = rotten[0];
                int c = rotten[1];
                
                for (int[] direction : directions) {
                    int dr = direction[0];
                    int dc = direction[1];

                    int newRow = r + dr;
                    int newCol = c + dc;

                    if (
                        newRow >= 0 &&
                        newRow < ROWS &&
                        newCol >= 0 &&
                        newCol < COLS &&
                        grid[newRow][newCol] == 1
                    ) {
                        grid[newRow][newCol] = 2;
                        freshCount -= 1;
                        queue.offer(new int[]{newRow, newCol});
                    }
                }
            }
            timer++;
        }

        return freshCount == 0 ? timer : -1;
    }
}
