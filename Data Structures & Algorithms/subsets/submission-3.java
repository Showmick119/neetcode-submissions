class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        currSet = new ArrayList<>();
        subsets = new ArrayList<>();
        helper(0, currSet, subsets);
        return subsets;      
    }

    private void helper(int i, List<Integer> currSet, List<List<Integer>> subsets) {
        if (i >= nums.length) {
            subsets.add(new ArrayList<>(currSet));
            return;
        }

        // make a choice
        currSet.add(nums[i]);
        helper(i + 1, currSet, subsets);

        // undo the choice
        currSet.remove(curr.size() - 1);
        helper(i + 1, currSet, subsets);
    }
}
