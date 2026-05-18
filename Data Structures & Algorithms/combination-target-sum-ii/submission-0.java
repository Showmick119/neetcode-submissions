class Solution {
    private List<List<Integer>> combos;

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        // each element chosen at once, so can't go that extreme
        // HashMap?
        Arrays.sort(candidates);
        combos = new ArrayList<>();
        List<Integer> curr = new ArrayList<>();
        helper(0, candidates, target, curr);
        return combos;
    }

    private void helper(int i, int[] candidates, int target, List<Integer> curr) {
        if (target == 0) {
            combos.add(new ArrayList<>(curr));
            return;
        }
        if (i >= nums.length || target <= 0) {
            combos.add(new ArrayList<>(curr));
            return;
        }

        curr.add(candidates[i]);
        helper(i + 1, candidates, target - candidates[i], curr);
        
        curr.remove(curr.size() - 1);
        while (i + 1 < candidates.length && candidates[i] == candidatees
        [i + 1]) {
            i++;
        }
        helper(i + 1, candidates, target, curr);
    }
}
