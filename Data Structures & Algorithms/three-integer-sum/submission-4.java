class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Set<List<Integer>> set = new HashSet<>();
        Arrays.sort(nums);

        for (int i = 0; i < nums.length; i++) {
            List<Integer> temp = new ArrayList<>();
            // we don't want to use the same starting element twice
            // this check works due to the array being sorted
            if (nums[i] > 0) break;
            if ((i > 0) && (nums[i] == nums[i - 1])) {
                continue;
            }
            int L = i + 1;
            int R = nums.length - 1;
            while (L < R) {
                if ((nums[L] + nums[R] + nums[i]) > 0) {
                    R--;
                } else if ((nums[L] + nums[R] + a) < 0) {
                    L++;
                } else {
                    set.add(Arrays.asList(nums[L], nums[R], nums[i]));
                    L++;
                    R--;
                }
            }
        }
        // make sure to convert the Set to List, such that we match
        // the given return type
        return new ArrayList<>(set);
    }
}