class Solution {
    int[][] directions = {
        {1, 0},
        {-1, 0},
        {0, 1},
        {0, -1}
    };
    public int numIslands(char[][] grid) {
        // Using dfs
        // We traverse through each position in the grid and do a
        // search from there.
        int ROWS = grid.length;
        int COLS = grid[0].length;
        int islands = 0;

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (grid[r][c] == '1') {
                    // point is to mark the grid
                    // no matter how big the group of 1s, the num of islands
                    // gets incremented by only 1
                    dfs(grid, r, c, ROWS, COLS);
                    islands++; // 1 group found
                }
            }
        }
        return islands;
    }

    private void dfs(char[][] grid, int r, int c, int ROWS, int COLS) {
        if (r < 0 || c < 0 || r >= ROWS || c >= COLS || grid[r][c] == '0') {
            return;
        }
        grid[r][c] = '0';
        for (int[] dir : directions) {
            int nr = r + dir[0], nc = c + dir[1];
            dfs(grid, nr, nc, ROWS, COLS);
        }
    }
}
