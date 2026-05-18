class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> set = new HashSet<>();
        int L = 0;
        int maxLength = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(L) == s.charAt(R)) {
                L++;
                maxLength = Math.max(maxLength, (R - L + 1))
            } else if (s.charAt(L) != s.charAt(R)) {
                R++;
            }
        }
        return maxLength;
    }
}
