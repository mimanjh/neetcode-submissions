class Solution {
    private int ROWS;
    private int COLS;
    private char[][] GRID;

    public int numIslands(char[][] grid) {
        // dfs to find areas of 1 surrounded by 0s and edge
        // loop through all values
        // check if the value is 1
        // if it is, dfs
        // each time dfs finishes, increment island count by 1
        // in dfs, default case would be if it goes over the outside boundary
        // or meets a 0
        // other cases, set 1 to 0, so it doesn't count it anymore
        // spread to all other directions

        ROWS = grid.length;
        COLS = grid[0].length;
        GRID = grid;
        int numOfIslands = 0;

        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j < COLS; j++) {
                if (grid[i][j] == '1') {
                    dfs(i, j);
                    numOfIslands += 1;
                }
            }
        }

        return numOfIslands;
    }

    private void dfs(int row, int col) {
        if (
            row >= ROWS ||
            row < 0 ||
            col >= COLS ||
            col < 0 ||
            GRID[row][col] == '0'
        ) {
            return;
        }

        GRID[row][col] = '0';

        dfs(row + 1, col);
        dfs(row - 1, col);
        dfs(row, col + 1);
        dfs(row, col - 1);
    }

}
