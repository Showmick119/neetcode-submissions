class Solution {
    public int maxProfit(int[] prices) {
        int max = 0;
        for (int i = 0; i < prices.length; i++) {
            for (int j = 1 + i; j < prices.length; j++) {
                int curr = prices[j] - prices[i];
                max = Math.max(max, curr);
            }
        }
        return max;
    }
}
