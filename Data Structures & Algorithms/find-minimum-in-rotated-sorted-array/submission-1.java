class Solution {
    public int findMin(int[] nums) {
        // essentially the array is not sorted and we need to write the
        // algorithm to sort it
        int L = 0, R = nums.length - 1;
        int M = (L + R) / 2;
        int res = nums[M];

        while (L <= R) {
            // check if it already sorted
            // if already sorted then just take the left most value
            if (nums[L] < nums[R]) {
                res = Math.min(res, nums[L]);
                break;  // no need to check as we are already sorted               
            }
            
            if (nums[M] >= nums[L]) {
                L = M + 1;
                M = (L + R) / 2;
                res = Math.min(res, nums[M]);
            } else {
                R = M - 1;
                M = (L + R) / 2;
                res = Math.min(res, nums[M]);
            }
        }
        return res;
    }
}
