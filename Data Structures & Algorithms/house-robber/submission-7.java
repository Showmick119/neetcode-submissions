class Solution {
    public int rob(int[] nums) {
        /* dp array will store the max money from houses upto the
        ith house. So it's a summation of several houses.
        Whereas, nums stores the amount of money the ith house has.
        Specifically, how much money one house has.
        */
        if (nums.length == 1) {
            return nums[0];
        } else if (nums.length == 2) {
            // return (nums[0] > nums[1]) ? nums[0] : nums[1];
        }
        int[] dp = new int[nums.length + 1];
        int max = 0;
        dp[0] = nums[0]; // base case
        dp[1] = nums[1]; // base case
        // dp[i] is the best answer for subproblem upto index i
        for (int i = 2; i < nums.length; i++) {
            dp[i] = nums[i] + dp[i - 2];
            max = Math.max(dp[i], dp[i - 1]);
        }
        return max;
    }
}

/*
We have a decision tree. At each house, we have to make the choice of
robbing it or skipping it.

- If you rob house i, you get nums[i], price of ith house. You also
get max money from houses up to index (i - 2). 
- You cannot rob (i - 1), since you are not allowed to rob adjacent
houses.
- If you skip house i, you get max money from houses upto (i - 1), its
adjacent house.
- If you skip current house (i), the max money you have till that point
is in dp[i - 1]. Max stored in it's adjacent, previous house.
- The solution for nth house, depends only on solutions of the (n - 1)
and (n - 2) houses.
- We have 2 starting points, i = 0 and i = 1. And each ith sum of
robbing, depends on the current nums[i] value, and how much we had
robbed till (i - 2).
- So we choose: is current price + how much we've stored till now, 
better than what we've stored till i - 1, the other adjacent house.
*/