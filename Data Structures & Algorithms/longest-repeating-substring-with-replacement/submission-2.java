class Solution {
    public int characterReplacement(String s, int k) {
        Map<Character, Integer> map = new HashMap<>();
        int L = 0, R = 0;
        int maxLength = 0;
        // no need to store R, as R will only increment
        // but L will only increment when a certain condition met
        // Collections.max(map.values()) ---> get max character count 
        while (R < s.length()) {
            map.put(s.charAt(R), map.getOrDefault(s.charAt(R), 0) + 1);
            int windowLen = R - L + 1;
            if ((windowLen - Collections.max(map.values())) <= k) {
                maxLength = Math.max(maxLength, windowLen);
            } else {
                L++;
                // R--;
            }
            R++;
        }
        return maxLength;
    }
}
