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

        currSet.remove(currSet.size() - 1);
        // we do not want to try the element at index (currSet.size() - 1)
        // but we ALSO DO NOT WANT TO TRY IT'S DUPLICATES. SO we have to
        // skip and make sure that, right after removing X, we just end up
        // adding and exploring with it's duplicate. That defies the whole
        // point.
        while ((i + 1 < nums.length) && (nums[i] == nums[i + 1])) {
            i++;
        }
        helper (i + 1, nums, currSet, subsets);
    }
}
