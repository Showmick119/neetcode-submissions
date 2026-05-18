class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Set<List<Integer>> set = new HashSet<>();
        Arrays.sort(nums);
        int L = 0;
        int R = nums.length - 1;

        for (int i = 0; i < nums.length; i++) {
            List<Integer> temp = new ArrayList<>();
            // we don't want to use the same starting element twice
            // this check works due to the array being sorted
            if ((i > 0) && (nums[i] == nums[i - 1])) {
                continue;
            }
            int a = nums[i];
            while (L < R) {
                if ((nums[L] + nums[R] + a) > target) {
                    R--;
                } else if ((nums[L] + nums[R] + a) < target) {
                    L++;
                } else {
                    temp.add(a);
                    temp.add(nums[L]);
                    temp.add(nums[R]);
                }
            }
            set.add(temp);
        }
        // make sure to convert the Set to List, such that we match
        // the given return type
        return new ArrayList<>(set);
    }
}