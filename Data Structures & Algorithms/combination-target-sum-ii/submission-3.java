class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        // each element can be chosen at most once
        List<Integer> currSet = new ArrayList<>();
        List<List<Integer>> subsets = new ArrayList<>();
        helper(0, candidates, target, currSet, subsets);
        return subsets;
    }

    private void helper(int i, int[] candidates, int target, List<Integer> currSet, List<List<Integer>> subsets) {
        if (target == 0) {
            subsets.add(new ArrayList<>(currSet));
            return;
        }

        // exceeded target value, hence returning back. Now, the next
        // operation after BACKTRACKING is to make the other decision
        // of removing that element, till it no longer exceeds target.
        // And trying other values which could potentially lead to target.
        if (target <= 0 || i >= nums.length) {
            return; 
        }

        currSet.add(nums[i]);
        helper(i + 1, candidates, target - nums[i], currSet, subsets);

        currSet.remove(currSet.size() - 1);
        helper(i + 1, candidates, target - nums[i], currSet, subsets);
    }

}
