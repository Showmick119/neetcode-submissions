class Solution {
    public int minCostClimbingStairs(int[] cost) {
        /*
        Suppose you go two steps or one step from index i. No matter
        how many steps you take, it will cost whatever is the ith
        value in the cost array.

        You want to take the step, to i + 1 floor or i + 2 floor,
        based on whichever one can lead to a minimum cost to reach
        the top.

        The position after the final index is the "top position",
        not the final index itself. We want to go "out of bounds" as
        early as possible.
        */
        for (int i = 2; i < cost.length; i++) {
            cost[i] += Math.min(cost[i - 1], cost[i - 2]);
        }
        return Math.min(cost[cost.length - 1], cost[cost.length - 2]);
    }
}
