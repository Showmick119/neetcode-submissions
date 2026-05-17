class Solution {
    public String longestPalindrome(String s) {
        int resLen = 0;
        int resIdx = 0;

        for (int i = 0; i < s.length(); i++) {
            // odd length
            int l = i;
            int r = i; // Since it's odd, there's only 1 center, hence
            // both our l and r pointers will start expanding out of
            // the same index.
            while (l >= 0 && r < s.length() && 
                    s.charAt(l) == s.charAt(r)) {
                if (r - l + 1 > resLen) {
                    resIdx = l;
                    resLen = r - l + 1;
                }
                l--;
                r++;
            }

            // even length
            l = i;
            r = i + 1; // When it's even, we have 2 elements in the
            // center. A left-center and a right-center. Hence, we 
            // cannot have one center, like we did in odd lengths.
            while (l >= 0 && r < s.length() &&
                    s.charAt(l) == s.charAt(r)) {
                if (r - l + 1 > resLen) {
                    resIdx = l;
                    resLen = r - l + 1;
                }
                l--;
                r++;
            }
        }

        return s.substring(resIdx, resIdx + resLen);
    }
}
