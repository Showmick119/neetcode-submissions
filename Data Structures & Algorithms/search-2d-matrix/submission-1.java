class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int ROWS = matrix.length;
        int COLS = matrix[0].length;

        int l = 0;
        int r = ROWS * COLS - 1; // Since we are flattening 1D -> 2D

        while (l < r) {
            int mid = (l + r) / 2;
            int row = mid / COLS;
            int col = mid % COLS;

            if (target < matrix[row][col]) {
                r = mid - 1;
            } else if (target > matrix[row][col]) {
                l = mid + 1;
            } else {
                return true;
            }
        }
        return false;
    }
}
