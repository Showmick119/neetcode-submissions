class Solution {
    public int search(int[] nums, int target) {
        // they didn't say the array 'might' be rotated
        // IT IS ROTATED FOR SURE
        // the index is from the current array, not the original 
        // non-rotated array
        // the values of the array are not continuous like 1, 2, 3...

        int l = 0, r = nums.length - 1;
        int m = (l + r) / 2;

        while (l <= r) {
            if (nums[l] < nums[r]) {
                if (target < nums[m]) {
                    r = m - 1;
                } else if (target > nums[m]) {
                    l = m + 1;
                } else {
                    return m;
                }
            }

            // how do we know if we want to search left portion (big)
            // or if we want to search right portion (small)
            if (target > nums[m]) {
                if (nums[l] <= nums[m]) {
                    l = m + 1;
                } else {
                    r = m - 1;
                }
            } else if (target < nums[m]) {
                if (nums[l] <= nums[m]) {
                    l = m + 1;
                } else {
                    r = m - 1;
                }
            } else {
                return m;
            }
        }
        return -1;
    }
}
