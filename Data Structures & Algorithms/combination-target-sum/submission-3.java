class Solution {
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> combos = new ArrayList<>();
        List<Integer> currComb = new ArrayList<>();
        helper(0, nums, target, currComb, combos);
        return combos;
    }

    private void helper(int i, int[] nums, int target, List<Integer> currComb, List<List<Integer>> combos) {
        if (target == 0) {
            combos.add(new ArrayList<>(currComb));
            return;
        }
        if (target < 0 || i >= nums.length) {
            return;
        }

        currComb.add(nums[i]);
        helper(i, nums, target - nums[i], currComb, combos);

        currComb.remove(currComb.size() - 1);
        // as we didn't add anything and didn't build up towards our
        // target. We cannot substract from target. Rather we skip
        // over the current index and move on to the next index.
        helper(i + 1, nums, target, currComb, combos);

        // EXPLORED TWO EXTREMES. One where you keep skipping indexes
        // and don't build towards target. Another where you add the
        // same index and keep building towards target using the same
        // index. While exploring these two extremes, we also get what's
        // in between? Like adding different elements, etc.
    }
}
