class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> freqMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (!freqMap.containsKey(nums[i])) {
                freqMap.put(nums[i], 1);
            } else {
                freqMap.put(nums[i], freqMap.get(nums[i]) + 1);
            }
        }
        List<Map.Entry<Integer, Integer>> freqList = new ArrayList<>(freqMap.entrySet());
        freqList.sort(Map.Entry.comparingByValue());
        int[] toppers = new int[k];
        for (int i = 0; i < k; i++) {
            toppers[i] = freqList.get(freqList.size() - 1 - i).getKey();
        }
        return toppers;
    }
}
