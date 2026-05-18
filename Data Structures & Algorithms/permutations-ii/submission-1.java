class Solution {
    private Map<Integer, Integer> count;
    private List<List<Integer>> res;

    public List<List<Integer>> permuteUnique(int[] nums) {
        // Now we have duplicates. Use HashSet? No but that would also
        // take away our other permutations, since they all have same
        // value, but just different orders
        Arrays.sort(nums);
        res = new ArrayList<>();
        count = new HashMap<>();  // every key will be unique
        List<Integer> perm = new ArrayList<>();

        for (int num : nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }

        backtrack(0, perm);
        return res;
    }

    private void backtrack(int[] nums, List<Integer> perm) {
        // Decision Tree will be formed from the HashMap's Keys
        if (perm.size() == nums.length) { // perm complete, no more values to add
            res.add(new ArrayList<>(perm));
            return res;
        }

        for (int num : count.keySet()) {
            if (count.get(num) > 0) { // checking frequency of that num
                perm.add(num);
                count.put(num, count.get(num) - 1);

                // would've cleaned up and returned result eventually
                dfs(nums, perm);

                // add back, opposite action
                count.put(num, count.get(num) + 1);
                perm.remove(perm.size() - 1);
            }
        }
    }
}