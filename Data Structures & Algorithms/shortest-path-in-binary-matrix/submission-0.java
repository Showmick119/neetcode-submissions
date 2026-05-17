class Solution {
    int[][] directions = {
        {1, 0},
        {-1, 0},
        {0, 1},
        {0, -1},
        {1, -1},
        {-1, 1},
        {1, 1},
        {-1, -1}
    };

    public int shortestPathBinaryMatrix(int[][] grid) {
        int ROWS = grid.length;
        int COLS = grid.length;
        // grid[i][j] can be 0 or 1. Which includes the top-left and
        // bottom-right.
        if (grid[0][0] == 1 || grid[ROWS - 1][COLS - 1] == 1) {
            return -1;
        } // checking for edge case
        
        Queue<int[]> q = new LinkedList<>();
        // we already checked that it's not 1, hence we were able to
        // visit it. But now after visiting, we must set it to 1, such
        // that we do not visit it again.
        q.add(new int[]{0, 0, 1});
        // each visited cell counts as length = 1
        grid[0][0] = 1;

        while (!q.isEmpty()) {
            int[] curr = q.poll();
            int r = curr[0], c = curr[1], length = curr[2];

            if (r == ROWS - 1 && c == COLS - 1) {
                return length;
            }

            for (int[] dir : directions) {
                int rows = r + dir[0];
                int cols = c + dir[1];

                if (rows >= 0 && cols >= 0 && rows < ROWS &&
                cols < COLS && grid[rows][cols] == 0) {
                    q.offer(new int[]{rows, cols, length + 1});
                    grid[rows][cols] = 1;
                }
            }
        }
        return -1;
    }
}