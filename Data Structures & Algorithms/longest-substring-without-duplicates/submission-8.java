class Solution {
    public int lengthOfLongestSubstring(String s) {
        s = s.replaceAll("\\s+", "").toLowerCase();
        // sliding window with variable length k
        int max = 0; // since L and R start together and have a window
        // of 1
        int L = 0;
        for (int R = 0; R < s.length(); R++) {
            if (s.charAt(L) == s.charAt(R)) {
                max = Math.max(max, R - L + 1);
                L++;
            } else {
                continue;
            }
        }
        return max;
    }
}
