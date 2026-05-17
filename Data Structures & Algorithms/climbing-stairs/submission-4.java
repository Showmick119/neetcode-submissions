class Solution {
    public int climbStairs(int n) {
        int one = 1;
        int two = 1;
        
        for (int i = 1; i < n; i++) {
            int temp = two;
            two = one + two;
            one = temp;
        }
        return two;
    }
}
