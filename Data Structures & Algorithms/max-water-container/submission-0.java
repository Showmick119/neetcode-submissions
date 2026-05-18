class Solution {
    public int maxArea(int[] heights) {
        // solving with two pointers logic
        // we want height to be as low as possible and width to be as
        // high as possible
        int L = 0;
        int R = heights.length - 1;
        int maxArea = 0;

        while (L < R) {
            int height = Math.min(heights[L], heights[R]);
            int width = R - L + 1;
            int area = height * width;
            maxArea = Math.max(maxArea, area);

            if (heights[L] <= heights[R]) {
                R--;
            } else {
                L++;
            }
        }
        return maxArea;
    }
}
