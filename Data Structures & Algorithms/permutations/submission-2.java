class Solution {
    public List<List<Integer>> permute(int[] nums) {
        return helper(0, nums);
    }

    private List<List<Integer>> helper(int i, int[] nums) {
        if (i >= nums.length) {
            List<List<Integer>> subsets = new ArrayList<>();
            subsets.add(new ArrayList<>());
            return subsets;
        }

        List<List<Integer>> subsets = new ArrayList<>();
        List<List<Integer>> currSet = helper(i + 1, nums);
        
        for (List<Integer> curr : currSet) {
            for (int j = 0; j < curr.size() + 1; j++) {
                List<Integer> copy = new ArrayList<>();
                copy.addAll(curr);
                copy.add(j, nums[i]);
                subsets.add(copy);
                // currSet.add(j, nums[i]);
            }
        }
        return subsets;
    }
}
