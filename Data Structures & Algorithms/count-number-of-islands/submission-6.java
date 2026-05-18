class Solution {
    public int[][] directions = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
    
    public int numIslands(char[][] grid) {
        int ROWS = grid.length, COLS = grid[0].length;
        Set<int[]> visited = new HashSet<>();
        int islands = 0;

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (grid[r][c] == '1') {
                    bfs(grid, r, c, visited);
                    islands++;
                }
            }
        }
        return islands;
    }

    private void bfs(char[][] grid, int r, int c, Set<int[]> visited) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{r, c});
        visited.add(new int[]{r, c});

        while (!queue.isEmpty()) {
            int row = queue.poll()[0], col = queue.poll()[1];
            for (int[] dir : directions) {
                int nr = row + dir[0], nc = col + dir[1];
                if (nr >= 0 && nc >= 0 && nr < grid.length && nc < grid[0].length
                    && grid[nr][nc] == '1') {
                        queue.add(new int[]{nr, nc});
                        visited.add(new int[]{nr, nc});
                    }
            }
        }
    }
}
