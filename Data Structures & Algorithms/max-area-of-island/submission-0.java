class Solution {
    public int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public int maxAreaOfIsland(int[][] grid) {
        // bfs should return the area
        int maxArea = 0;
        int ROWS = grid.length, COLS = grid[0].length;

        // this is not the exploration, this is just starting at 
        // different points in the matrix and exploring all the possible
        // directions and counting the 1s we run into along the way
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (grid[r][c] == 1) {
                    int currArea = bfs(grid, r, c);
                    maxArea = Math.max(maxArea, currArea);
                }
            }
        }
        return maxArea;
    }

    private int bfs(int[][] grid, int r, int c) {
        Queue<int[]> q = new LinkedList<>();
        grid[r][c] = 0; // it's been passed into the method cause it was
        // on the grid. But now we set it's grid value to 0, since it's been visited
        // now, and is part of a island group.
        q.add(new int[]{r, c});
        int area = 1; // added new direction successfully, so increment area.

        while (!q.isEmpty()) {
            int[] curr = q.poll();
            
            for (int[] dir : directions) {
                int nr = curr[0] + dir[0], nc = curr[1] + dir[1];
                if (nr >= 0 && nc >= 0 && nr < grid.length && nc < grid[0].length
                && grid[nr][nc] == 1) { // checking if it follows path and requirements
                    q.add(new int[]{nr, nc});
/* increase area, each time we successully add a diretion, NOT EACH TIME 
WE POLL one. As from that poll we could have multiple successful directions 
that contribute to area, so doing just one one incrememnt wouldn't count 
all of them. */
                    grid[nr][nc] = 0;
                    area++;  // each time we successfully add new direction, increase area
                }
                
            }
        }
        return area;
    }
}
