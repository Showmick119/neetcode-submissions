class Solution {
    public int characterReplacement(String s, int k) {
        int L = 0;
        int max = 0;

        for (int R = 0; R < s.length(); R++) {
            if (s.charAt(L) == s.charAt(R)) {
                max = Math.max(max, (R - L + 1));
            } else {
                L++;
            }
        }
        return max + k;
    }
}
