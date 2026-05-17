class Solution {
    public boolean exist(char[][] board, String word) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (dfs(0, i, j, board, word)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean dfs(int i, int r, int c, char[][] board, String word) {
        if (i == word.length()) {
            return true;
        }
        if (r < 0 || c < 0 || r >= board.length || c >= board[0].length || 
        word.charAt(i) != board[r][c] || board[r][c] == '#') {
            return false;
        }

        // The word does exist at this index and is valid. Hence, mark
        // it with a symbol, denoting that you've visited it.
        board[r][c] = '#';
        // When we do our next exploration, all the recursive calls will
        // know that index (r, c) has been visited and it was part of 
        // the String.
        boolean res = (
                    dfs(i + 1, r + 1, c, board, word) ||
                    dfs(i + 1, r - 1, c, board, word) ||
                    dfs(i + 1, r, c + 1, board, word) ||
                    dfs(i + 1, r, c - 1, board, word)
                    );
        board[r][c] = word.charAt(i); // essentially the backtracking step of UN-DOING your action X
        /*
        You temporarily mark cells with '#' to avoid revisiting them 
        in the current path. But after exploring that path, you need 
        to undo the mark so other paths can use that cell.

        The board stays permanently marked with '#', breaking future
        searches that need those cells.
        */
        
        return res;
    }
}
