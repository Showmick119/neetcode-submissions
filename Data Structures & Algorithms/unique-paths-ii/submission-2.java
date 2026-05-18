class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        // Bottom up approach, again building up from the bottom
        // We are not using DFS/BFS like we do in Graphs
        int ROWS = obstacleGrid.length;
        int COLS = obstacleGrid[0].length;
        int[] prevRow = new int[COLS];
        for (int i = ROWS - 1; i >= 0; i--) {
            int[] currRow = new int[COLS];
            for (int j = COLS - 1; j >= 0; j--) {
                if (i == ROWS - 1 && j == COLS - 1) {
                    currRow[j] = 1;
                } else if (obstacleGrid[i][j] == 1) {
                    currRow[j] = 0;
                } else {
                    if (j + 1 < COLS) {
                        currRow[j] = prevRow[j] + currRow[j + 1];
                    } else {
                        currRow[j] = prevRow[j];
                    }
                }
            }
            prevRow = currRow;
        }
        return prevRow[0];
    }
}