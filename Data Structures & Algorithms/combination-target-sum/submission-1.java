class Solution {
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> combos = new ArrayList<>();
        List<Integer> currComb = new ArrayList<>();
        helper(0, nums, target, currComb, combos);
        return combos;
    }

    private void helper(int i, int[] nums, int target, List<Integer> currComb, List<List<Integer>> combos) {
        if (currComb.stream().mapToInt(Integer::intValue).sum() == target) {
            combos.add(new ArrayList<>(currComb));
            return;
        }
        // Having one base case is sufficient. Two is not always needed.
        currComb.add(nums[i]);
        helper(i + 1, nums, target, currComb, combos);

        currComb.remove(currComb.size() - 1);
        helper(i + 1, nums, target, currComb, combos);
        
        // currComb.add(nums[i]);
        // helper(i, nums, target, currComb, combos);

        // currComb.remove(currComb.size() - 1);
        // helper(i, nums, target, currComb, combos);
    }
}
