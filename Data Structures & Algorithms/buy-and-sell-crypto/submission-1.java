class Solution {
    public int maxProfit(int[] prices) {
        int l = 0;
        int r = 1;
        int max = 0;
        while (r < prices.length) {
            if (prices[r] > prices[l]) {
                max = Math.max((prices[r] - prices[l]), max);
            } else {
                // we are buying at too expensive a day. So shift day.
                l = r;
            }
            r++;
        }
        return max;
    }
}
