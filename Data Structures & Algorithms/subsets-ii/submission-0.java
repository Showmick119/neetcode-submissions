class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> subsets = new ArrayList<>();
        List<Integer> currSet = new ArrayList<>();
        helper(0, nums, currSet, subsets);
        return subsets;
    }

    private void helper(int i, int[] nums, List<Integer> currSet, List<List<Integer>> subsets) {
        if (i >= nums.length) {
            subsets.add(new ArrayList<>(currSet));
            return;
        }
        currSet.add(nums[i]);
        helper(i + 1, nums, currSet, subsets);
        currSet.remove(currSet.size() - 1); // remove most recently added

        while ((i < nums.length) && (nums[i] == nums[i + 1])) {
            i++;
        }
        helper(i, nums, currSet, subsets);
    }
}
