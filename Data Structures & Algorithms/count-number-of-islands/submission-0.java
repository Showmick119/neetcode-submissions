class Solution {
    public int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
 
    public int numIslands(char[][] grid) {
        int r = grid.length, c = grid[0].length;
        int islands = 0;

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (grid[r][c] == '1') {
                    dfs(grid, r, c);
                    islands++;
                }
            }
        }         
    }

    private void dfs(char[][] grid, int r, int c) {
        if (r < 0 || c < 0 || r == grid.length || c = grid[0].length
        || grid[r][c] == '0') {
            return;
        }

        grid[r][c] = '0'; // marking it as visited and part of a
        // group of islands
        
        for (int[] dir : directions) {
            dfs(grid, r + dir[0], c + dir[1]);
        }
    }
}
