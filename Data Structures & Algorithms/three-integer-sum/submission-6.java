class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // The naive solution is O(n^3), where we use 3 for-loops
        Arrays.sort(nums);
        Set<List<Integer>> triplets = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            int l = i + 1;
            int r = nums.length - 1;
            while (l < r && l < nums.length) {
                if (nums[l] + nums[r] + nums[i] == 0) {
                    triplets.add(Arrays.asList(nums[i], nums[l], nums[r]));
                    l++;
                    r--;
                } else if (nums[l] + nums[r] + nums[i] < 0) {
                    l++;
                } else if (nums[l] + nums[r] + nums[i] > 0) {
                    r--;
                }
            }
        }
        return new ArrayList<>(triplets);
    }
}
