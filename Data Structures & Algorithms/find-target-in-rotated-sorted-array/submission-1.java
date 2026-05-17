class Solution {
    public int search(int[] nums, int target) {
        // they didn't say the array 'might' be rotated
        // IT IS ROTATED FOR SURE, AT LEAST ONCE
        // the index is from the current array, not the original 
        // non-rotated array
        // the values of the array are not continuous like 1, 2, 3...

        int l = 0, r = nums.length - 1;

        while (l <= r) {
            int mid = (l + r) / 2;

            if (nums[mid] == target) {
                return mid;
            }

            if (nums[l] <= nums[mid]) {
                if (target > nums[mid] || target < nums[l]) {
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            } else {
                if (target < nums[mid] || target > nums[r]) {
                    r = mid - 1;
                } else {
                    l = mid + 1; 
                    // already inside right small portion, but need to check it's
                    // bigger elements which are more to the right obviously
                }
            }
        }
        return -1;
    }
}
