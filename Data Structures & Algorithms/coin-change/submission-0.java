class Solution {
    public int coinChange(int[] coins, int amount) {
        // Edge Case
        if (amount == 0) {
            return 0;
        }
        int[] dp = new int[amount + 1]; // If amount is 7, we want
        // till index 7. So index 0 to index 7, total of 8 elements.
        
        // Initialize the dp array to a larger value, such that, we can
        // get it's accurate value, even with the Math.min()
        for (int i = 0; i < dp.length; i++) {
            dp[i] = amount + 1;
        }

        // Creating our base case
        dp[0] = 0; // will build up from our base case
        // We will build up for all the amounts, leading to amount, and
        // then return dp[amount], which is the final one we build
        for (int a = 1; a < amount + 1; a++) {
            for (int coin : coins) {
                // Suppose we are using coin value 5. Even though we are
                // using coin value 5, it is still 1 SINGULAR coin. So,
                // in terms of building up to amount 'a', the amount of
                // coins being used is 1, when we add 5. But, then we
                // still need another coin to be added, and it's value
                // has to be amount - coin, since coin = 5, is already
                // contributing value to build up to amount, while only
                // using 1 tangible coin.
                if (a - coin >= 0) {
                    // We only want to store the minimum number of coins
                    // taken to reach that point.
                    dp[a] = Math.min(dp[a], 1 + dp[a - coin]);;
                    // number of coins to get X dollars, where X is the
                    // value of coin. And also the number of coins to
                    // get Y dollars, where Y is amount - coin, so the
                    // number of coins to build Y dollars.
                }
            }
        }

        return (dp[amount] != amount + 1) ? dp[amount] : -1;
    }
}
