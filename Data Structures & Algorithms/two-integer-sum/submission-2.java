class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }
        for (int i = 0; i < nums.length; i++) {
            int num2 = target - nums[i];
            if (map.containsKey(num2) && map.get(num2) != i) {
                return new int[]{i, map.get(num2)};
            }
        }
        return new int[]{};
    }
}
