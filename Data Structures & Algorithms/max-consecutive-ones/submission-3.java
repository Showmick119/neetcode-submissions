class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxCount = 0;
        int currCount = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                currCount++;
            } else {
                // we can't just keep changing maxCount each time we have a new sequence
                // we only update it, if the new sequence is longer than previously stored
                // maxCount. And to check that, we use Math.max() 
                maxCount = Math.max(maxCount, currCount);
                currCount = 0;
            }
        }
        if (currCount > maxCount) {
            maxCount = currCount;
        }
        return maxCount;
    }
}