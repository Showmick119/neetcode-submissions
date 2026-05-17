class Solution {
    public void solve(char[][] board) {
        int ROWS = board.length;
        int COLS = board[0].length;

        for (int r = 0; r < ROWS; r++) {
            if (board[r][0] == 'O') {
                capture(board, r, 0);
            }
            if (board[r][COLS - 1] == 'O') {
                capture(board, r, COLS - 1);
            }
        }

        for (int c = 0; c < COLS; c++) {
            if (board[0][c] == 'O') {
                capture(board, 0, c);
            }
            if (board[ROWS - 1][c] == 'O') {
                capture(board, ROWS - 1, c);
            }
        }

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (board[r][c] == 'O') {
                    board[r][c] = 'X';
                } else if (board[r][c] == 'T') {
                    board[r][c] = 'O';
                }
            }
        }
    }

    // If invalid then discard and don't set the 'O' to 'T'
    // We want to find the group of 'O' which starts from borders
    // set them all to 'T'. These 'T', at the end will get converted
    // back to 'O', since they are connected to border and hence not
    // flippable to 'X'. But the 'O' which was not converted to 'T',
    // is NOT connected to the border, and hence is FLIPPABLE to 'X'.
    private void capture(char[][] board, int r, int c) {
        if (r < 0 || c < 0 || r >= board.length || c >= board[0].length ||
        board[r][c] == 'X' || board[r][c] == 'T') {
            return;
        }

        board[r][c] = 'T';
        // Traversing in all 4 directions and checking if there are
        // any other 'O' connected to the existing one, which could make
        // a group we're supposed to ignore.
        capture(board, r + 1, c);
        capture(board, r - 1, c);
        capture(board, r, c + 1);
        capture(board, r, c - 1);

        // why not backtrack? because we have no choices to make here.
        // We just have one simple task of DFS traversal and marking.
        // No option or requirement to explore different possibilities,
        // just have to explore a set path and mark. No choices to make,
        // thus backtracking is not needed in this dfs problem, just
        // a simple traversal and marking task.
    }
}
