class Solution {
    private int ROWS;
    private int COLS;

    public boolean exist(char[][] board, String word) {
        // dfs backtracking
        // visiting every value and spreading to all direction
        // to check if it's the next character
        // if not, return false
        // change the visited value to something else so that
        // it doesn't visit again and become an infinite loop

        ROWS = board.length;
        COLS = board[0].length;

        boolean result = false;
        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j < COLS; j++) {
                if (backtrack(board, word, i, j, 0)) {
                    return true;
                }
            }
        }
        return result;
    }

    private boolean backtrack(char[][] board, String word, int row, int col, int i) {
        if (i == word.length()) {
            return true;
        }

        if (
            row < 0 ||
            row >= ROWS ||
            col < 0 ||
            col >= COLS ||
            board[row][col] != word.charAt(i) ||
            board[row][col] == '#'
        ) {
            return false;
        }

        // choose
        board[row][col] = '#';
        // explore
        boolean result = backtrack(board, word, row + 1, col, i + 1) ||
                         backtrack(board, word, row - 1, col, i + 1) ||
                         backtrack(board, word, row, col + 1, i + 1) ||
                         backtrack(board, word, row, col - 1, i + 1);
        // undo
        board[row][col] = word.charAt(i);
        return result;
    }
}
