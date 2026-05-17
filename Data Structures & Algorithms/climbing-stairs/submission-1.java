class Solution {
    public int climbStairs(int n) {
        int one = 1;
        int two = 1;

        // if n = 5; we want it to iterate 4 times, hence we take
        // n - 1 = 4. So from 0, 1, 2, 3. We have 4 iterations.
        for (int i = 0; i < n - 1; i++) {
            int temp = one;
            one = one + two;
            two = temp;
        }

        return one;
    }
}
