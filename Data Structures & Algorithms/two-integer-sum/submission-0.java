class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = 1; j < nums.length; j++) {
                if (i != j || nums[i] + nums[j] == target) {
                    int[] array = {i, j};
                    return array;
                }
            }
        }
        return new int[]{};
    }
}
