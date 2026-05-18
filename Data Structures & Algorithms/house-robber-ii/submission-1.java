class Solution {
    public int rob(int[] nums) {
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
        dp[1] = nums[1];

        for (int i = 2; i < nums.length; i++) {
            if (i == nums.length - 1) {
                dp[i] = dp[i - 1];
            }  else {
                // You always take max, but you can only ADD to an index, 
                // when it's NOT ADJACENT. 
                dp[i] = Math.max(nums[i] + dp[i - 2], dp[i - 1]);
            }
            
        }
        return dp[nums.length - 1];
    } 
}

/*
- Since we can sum nums[1] + nums[4], it clearly does not follow some
pattern of only even or odd numbers, which are not adjacent.
- Instead it is that, given an index i, how can we maximize it's sum
with the rest of the array. 
*/