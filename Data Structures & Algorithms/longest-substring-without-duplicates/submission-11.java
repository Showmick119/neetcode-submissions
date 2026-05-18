class Solution {
    public int lengthOfLongestSubstring(String s) {
        int L = 0;
        int maxLength = 0;

        for (int R= 0; R < s.length(); R++) {
            if (s.charAt(L) == s.charAt(R)) {
                L++;
                maxLength = Math.max(maxLength, (R - L + 1));
            } else if (s.charAt(L) != s.charAt(R)) {
                R++;
            }
        }
        return maxLength;
    }
}
