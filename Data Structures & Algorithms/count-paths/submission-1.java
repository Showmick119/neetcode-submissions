class Solution {
    public int uniquePaths(int m, int n) {
        // In 1D DP, we need to store 2 variables for sliding accross
        // the array.
        // In 2D DP, we need to store 2 rows for sliding accross the
        // grid.
        int[] prevRow = new int[n];
        for (int j = m; j > 0; j--) {
            int[] currRow = new int[n];
            currRow[n - 1] = 1;
            for (int i = n - 2; i >= 0; i--) {
                currRow[i] = prevRow[i] + currRow[i - 1];
            }
            prevRow = currRow;
        }
        return prevRow[0];
    }
}
