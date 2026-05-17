class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<Integer> currSet = new ArrayList<>();
        List<List<Integer>> subsets = new ArrayList<>();
        helper(0, nums, currSet, subsets);
        return subsets;      
    }

    private void helper(int i, int[] nums, List<Integer> currSet, List<List<Integer>> subsets) {
        if (i >= nums.length) {
            subsets.add(new ArrayList<>(currSet));
            return;
        }

        // make a choice
        currSet.add(nums[i]);
        helper(i + 1, nums, currSet, subsets);

        // undo the choice
        currSet.remove(currSet.size() - 1);
        helper(i + 1, nums, currSet, subsets);
    }
}
