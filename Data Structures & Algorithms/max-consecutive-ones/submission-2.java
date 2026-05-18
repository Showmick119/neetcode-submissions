class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxCount = 0;
        int currCount = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                currCount++;
            } else {
                maxCount = currCount;
                currCount = 0;
            }
        }
        if (currCount > maxCount) {
            maxCount = currCount;
        }
        return maxCount;
    }
}