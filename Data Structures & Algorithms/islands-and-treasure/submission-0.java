class Solution {
    public void islandsAndTreasure(int[][] grid) {
        int[][] directions = {
            {1, 0},
            {-1, 0},
            {0, 1},
            {0, -1},
        };           // TRAVERSAL IN 4 DIRECTIONS!
        int INF = 2147483647;
        int ROWS = grid.length;
        int COLS = grid[0].length;
        boolean[][] visited = new boolean[ROWS][COLS];
        Queue<int[]> q = new LinkedList<>();

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (grid[r][c] == 0) {
                    q.offer(new int[]{r, c, 0}); // 0 because we start at 0 distance from the gate
                }
            }
        }

        while (!q.isEmpty()) {
            int queueLength = q.size();
            for (int i = 0; i < queueLength; i++) {
                int[] curr = q.poll();
                int dist = curr[2];
                
                for (int[] dir : directions) {
                    int nr = curr[0] + dir[0];
                    int nc = curr[1] + dir[1];

                    if (nr >= 0 && nc >= 0 && nr < grid.length &&
                    nc < grid[0].length && visited[nr][nc] == false
                    && grid[nr][nc] == INF) {
                        q.offer(new int[]{nr, nc, dist + 1});
                        grid[nr][nc] = dist + 1;
                        visited[nr][nc] = true;
                    }
                }
            }
        }
    }
}
