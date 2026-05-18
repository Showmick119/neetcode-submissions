class Solution {
    public int subarraySum(int[] nums, int k) {
        // No need for HashSet, as we don't care if it's a permutation
        // We can have same content, but different order
        
        // Considering the Edge Case:
        if (nums.length == 1) {
            if (nums[0] == k) {
                return 1;
            } else {
                return 0;
            }
        }

        int count = 0;
        int l = 0;
        for (int r = 0; r < nums.length; r++) {
            // Edge Case
            if (l == r) {
                if (nums[l] == k) {
                    count++;
                    l++;
                } else {
                    continue;
                }
            } else {
                int sum = 0;
                for (int i = l; i < r + 1; i++) {
                    sum += nums[i];
                }
                if (sum == k) {
                    count++;
                    l++;
                } else {
                    continue;
                }
            }
        }
        return count;

        // Even after a match, the pointers keep going forward
        // Sliding Window with two pointers
        // Each time the subarray is successful, we only increment r
        // pointer. Only when it is unsuccesful, do we increment the 
        // left pointer.

        // We use a for-loop in Sliding Window, and a while-loop in
        // Two Pointers.
        
        // It is O(n), since we pass through the array of n elements
        // only once. And it is O(1) space complexity, as we are not
        // creating any other data structures. We are simply returning
        // a value which will be stored in a primitive variable with
        // O(1) operations.
    }
}