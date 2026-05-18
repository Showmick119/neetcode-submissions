class Solution {
    public int countSubstrings(String s) {
        int count = 0;
        // Don't care about indexes here. Just want the number of
        // valid substrings. 'a' is a palindrome, since s.charAt(l)
        // equals s.charAt(r).

        for (int i = 0; i < s.length(); i++) {
            int l = i;
            int r = i;

            if (s.length() % 2 == 0) {
                l = i;
                r = i + 1;
                while (l >= 0 && r < s.length() && l <= r &&
                    s.charAt(l) == s.charAt(r)) {
                    l++;
                    r--;
                    count++;
                }
            } else {
                while (l >= 0 && r < s.length() && l <= r &&
                    s.charAt(l) == s.charAt(r)) {
                    l++;
                    r--;
                    count++;
                }
            }
        }
        return count;
    }
}
