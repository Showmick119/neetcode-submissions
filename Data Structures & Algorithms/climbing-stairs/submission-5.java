class Solution {
    public int climbStairs(int n) {
        int zero = 1; // ways to reach step 0
        int one = 1; // ways to reach step 1
        
        for (int i = 1; i < n; i++) {
            int temp = one; // we store the one which is ahead, since
            // it will get updated first
            one = one + zero;
            zero = temp;
        }
        return one;
    }
}
