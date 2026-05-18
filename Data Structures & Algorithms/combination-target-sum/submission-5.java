class Solution {
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<Integer> currSet = new ArrayList<>();
        List<List<Integer>> subsets = new ArrayList<>();
        helper(0, nums, target, currSet, subsets);
        return subsets;
    }

    private void helper(int i, int[] nums, int target, List<Integer> currSet, List<List<Integer>> subsets) {
        if (target == 0) {
            subsets.add(new ArrayList<>(currSet));
            return;
        }

        if (target <= 0 || i >= nums.length) {
            return
        }

        // make one extreme choice
        // for more-choices, a for-loop's used?
        currSet.add(nums[i]);
        helper(i, nums, target - nums[i], currSet, subsets); // don't increment i, as you want to use the same one

        // try no elements
        // somewhere in between you will get the middle of these two extremes
        // of trying same element and trying no elements
        currSet.remove(currSet.size() - 1);
        helper(i + 1, nums, target, currSet, subsets);
    }
}
