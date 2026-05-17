class Solution {
    public int rob(int[] nums) {
        if (nums.length == 0) {
            return 0;
        } else if (nums.length == 1) {
            return nums[0];
        } else if (nums.length == 2) {
            return (nums[0] > nums[1]) ? nums[0] : nums[1];
        }
        return Math.max(
            helper(Arrays.copyOfRange(nums, 0, nums.length - 1)),
            helper(Arrays.copyOfRange(nums, 1, nums.length))
        );
    }

    private int helper(int[] nums) {
        // We now have this new additional edge case
        if (nums.length == 0) {
            return 0;
        } else if (nums.length == 1) {
            return nums[0];
        } else if (nums.length == 2) {
            return (nums[0] > nums[1]) ? nums[0] : nums[1];
        }
        int[] dp = new int[nums.length];
        dp[0] = nums[0];
        dp[1] = Math.max(nums[1], nums[0]);

        for (int i = 2; i < nums.length; i++) {
            dp[i] = Math.max(nums[i] + dp[i - 2], dp[i - 1]);
        }
        return dp[nums.length - 1];
    } 
}

/*
- Since we can sum nums[1] + nums[4], it clearly does not follow some
pattern of only even or odd numbers, which are not adjacent.
- Instead it is that, given an index i, how can we maximize it's sum
with the rest of the array.
- Think in sub-problems, that we can be asked to give an answer from
any point in the array. That what was the max possible you could have
robbed from house 0 to house 2.
- NOT JUST house 0 to house N. It can also be from a smaller, minor
index. So keep this in mind, and solve with that mentality, that we
don't just want an answer at the end, but we want an answer at EACH
SMALLER SUB-PROBLEM TOO.
- And this mentality of wanting answer to each sub-problem, is what
leads to success in DP.
*/