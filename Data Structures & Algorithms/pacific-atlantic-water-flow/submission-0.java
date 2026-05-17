class Solution {
    int[][] directions = {
        {1, 0},
        {-1, 0},
        {0, 1},
        {0, -1}
    };
    public List<List<Integer>> both = new ArrayList<>();

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        // Using a DFS approach
        int ROWS = heights.length;
        int COLS = heights[0].length;
        boolean[][] pacVisit = new boolean[ROWS][COLS];
        boolean[][] atlVisit = new boolean[ROWS][COLS];
        
        // Vertical for-loop going through all the columns:
        // Top Pacific, Bottom ATL
        for (int i = 0; i < COLS; i++) {
            // pass in a default height value which is the same as 
            // the current one. This is because we don't know previous
            // height in this current position in the algorithm.
            // Only after entering the dfs, do we understand the previous
            // heights and its consequences.
            dfs(heights, 0, i, pacVisit, heights[0][i], ROWS, COLS);
            dfs(heights, ROWS - 1, i, atlVisit, heights[ROWS - 1][i], ROWS, COLS);
        }

        // Horizontal for-loop: Left side Pacific, Right Side ATL
        for (int i = 0; i < ROWS; i++) {
            dfs(heights, i, 0, pacVisit, heights[i][0], ROWS, COLS);
            dfs(heights, i, COLS - 1, atlVisit, heights[0][COLS - 1], ROWS, COLS);
        }

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (pacVisit[r][c] && atlVisit[r][c]) {
                    List<Integer> temp = new ArrayList<>();
                    temp.add(r);
                    temp.add(c);
                    both.add(temp);
                }
            }
        }
        return both;
    }

    private void dfs(int[][] heights, int r, int c, boolean[][] visit, int prev, int ROWS, int COLS) {
        visit[r][c] = true; // only valid ones passed in to begin with
        
        for (int[] dir : directions) {
            int nr = r + dir[0];
            int nc = c + dir[1];
            if (nr >= 0 && nc >= 0 && nr < ROWS && nc < COLS && !visit[nr][nc]
            && (heights[nr][nc] >= heights[r][c])) {
                dfs(heights, nr, nc, visit, heights[r][c], ROWS, COLS);
            }
        }
    }
}
