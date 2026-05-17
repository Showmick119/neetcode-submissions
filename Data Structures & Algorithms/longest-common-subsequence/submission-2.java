class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        // We will need to a 2D grid to do our dp iterations
        int[][] dp = new int[text1.length() + 1][text2.length() + 1];

        // In DP, you generally loop from the bottom right, all the
        // way up.
        for (int i = text1.length() - 1; i >= 0; i--) {
            for (int j = text2.length() - 1; j >= 0; j--) {
                if (text1.charAt(i) == text2.charAt(j)) {
                    dp[i][j] = 1 + dp[i + 1][j + 1]; // adding 1 +
                    // the diagonal
                } else {
                    dp[i][j] = Math.max(dp[i + 1][j], dp[i][j + 1]);
                }
            }
        }
        return dp[0][0];
    }
}

/*
- When we find a match we move diagonally.
- When we don't find a match, we go either right or down, and then the
max value from those 2, is placed at that index.
- It does feel like general DP, but a little tuned to this certain use
case.
*/