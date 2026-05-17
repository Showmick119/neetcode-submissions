class Solution {
    public int subarraySum(int[] nums, int k) {
        // Track how many times each prefix sum has occured
        Map<Integer, Integer> map = new HashMap<>();
        int count = 0;
        int sum = 0;
        // Sum of 0 happens once (1 frequency)
        // To correctly count subarrays that start from index 0
        map.put(0, 1);

        for (int num : nums) {
            sum += num;
            count += map.getOrDefault(sum - k, 0);
            map.put(sum, map.getOrDefault(sum, 0) + 1);
        }
        return count;
    }
}