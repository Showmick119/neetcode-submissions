class Solution {
    public int lengthOfLongestSubstring(String s) {
        s = s.replaceAll("\\s+", "").toLowerCase();
        // sliding window with variable length k
        int max = 0; // since L and R start together and have a window
        int count = 0;
        // of 1
        int L = 0;
        for (int R = 0; R < s.length(); R++) {
            if (s.charAt(L) == s.charAt(R)) {
                L = R;
                max = Math.max(max, count);
                count = 1;
            } else {
                count++;
            }
        }
        return count;
    }
}
