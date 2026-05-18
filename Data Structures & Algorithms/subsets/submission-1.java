class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        // what is the base case?
        // need a dfs helper method
        List<List<Integer>> subsets = new ArrayList<>();
        List<Integer> currSet = new ArrayList<>();
        helper(0, nums, currSet, subsets);
        return subsets;
    }

    private void helper(int i, int[] nums, List<Integer> currSet, List<List<Integer>> subsets) {
        if (i >= nums.length) {
            subsets.add(currSet);
            return;
        }
        currSet.add(nums[i]);
        helper(i + 1, nums, currSet, subsets);
        // only one has been added, so remove the most recent addition
        currSet.remove(currSet.size() - 1);
        helper(i + 1, nums, currSet, subsets);
    }
}
