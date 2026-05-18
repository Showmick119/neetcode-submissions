class Solution {
    int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public int orangesRotting(int[][] grid) {
        Deque<int[]> dq = new LinkedList<>();
        int time = 0, fresh = 0;
        int ROWS = grid.length, COLS = grid[0].length;

        // O(n * m) due to nested-loop
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (grid[r][c] == 1) {
                    fresh++;
                } else if (grid[r][c] == 2) {
                    dq.add(new int[]{r, c});
                }
            }
        }

        // going through for-loop and popping all the current elements
        while (!dq.isEmpty() && fresh > 0) {
            for (int i = 0; i < dq.size(); i++) {
                int[] curr = dq.remove();
                
                // not O(n), constant time, as we know it's always going to loop exactly 4 times
                for (int[] dir : directions) {
                    int nr = curr[0] + dir[0], nc = curr[1] + dir[1];
                    if (nr >= 0 && nc >= 0 && nr < grid.length && nc < grid[0].length
                    && grid[nr][nc] == 1) {
                        grid[nr][nc] = 2; // have to make sure we update the grid and clarify that this orange is NOW ROTTEN
                        dq.add(new int[]{nr, nc});
                        fresh--;
                    }
                }
            }
            time++;
        }

        return (fresh == 0) ? time : -1; 
        // if (fresh == 0) {
        //     return time;
        // } else {
        //     return -1;
        // }
    }
}