class Solution {
    public List<List<Integer>> permute(int[] nums) {
        return backtrack(0, nums);
    }

    private List<List<Integer>> backtrack(int i, int[] nums) {
        if (i == nums.length) {
            List<List<Integer>> res = new ArrayList<>();
            res.add(new ArrayList<>());
            return res;
        }

        List<List<Integer>> resPerm = new ArrayList<>();
        List<List<Integer>> perms = backtrack(i + 1, nums);

        for (List<Integer> curr : perms) {
            for (int j = 0; j < curr.size() + 1; j++) {  // + 1 as there's an extra spot we can add to
                List<Integer> currCopy = new ArrayList<>();
                currCopy.addAll(curr);  // not adding list inside list, rather all elements of that list getting copied in
                currCopy.add(j, nums[i]); // add the same element at multiple different positions
                resPerm.add(currCopy);
            }
        }
        return resPerm;
    }
}
