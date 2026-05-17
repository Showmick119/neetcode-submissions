class Solution {
    public int rob(int[] nums) {
        /* dp array will store the max money from houses upto the
        ith house. So it's a summation of several houses.
        Whereas, nums stores the amount of money the ith house has.
        Specifically, how much money one house has.
        */

        // EDGE CASE
        if (nums.length == 1) {
            return nums[0];
        // EDGE CASE
        } else if (nums.length == 2) {
            return (nums[0] > nums[1]) ? nums[0] : nums[1];
        }
        int[] dp = new int[nums.length];
        int max = 0;
        dp[0] = nums[0]; // base case
        // Mentality: If we were to end our problem right here, at
        // index 1, what would be our answer? This broken down, sub-
        // problem mentality is what will help solve these questions.
        dp[1] = Math.max(nums[1], nums[0]); // base case
        // dp[i] is the best answer for subproblem upto index i
        for (int i = 2; i < nums.length; i++) {
            // Max stored till index i, or max stored till previous
            // adjacent i. We cannot add (i) and (i - 1), but we can
            // definitely compare them, to answer sub-problem of which
            // is currently the greatest. 
            dp[i] = Math.max(nums[i] + dp[i - 2], dp[i - 1]);
        }
        // So what was our max, after traversing through the entire
        // array.
        // We want max value collected till final index, so we return
        // the dp value at final index.
        return dp[nums.length - 1];
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

- We are given a line of houses. But treat it as a smaller problem.
Whereas, instead of thinking about all these houses, at each iteration
we just think about 2 houses and choosing the best out of those 2.
This broken down smaller mentality will allow us to get the best house
on the long run.
- nums array and dp array is very different. dp array is simply for
storing the max upto that point.
- Each dp[i] should be self-contained, what's the maximum money we can
make, if the problem ended right here. This way future calculations can
trust that the previous ones made optimal choices.
- DP is about building a CHAIN of trust. Each link dp[i] must meet its
conditions as well as possible.
*/