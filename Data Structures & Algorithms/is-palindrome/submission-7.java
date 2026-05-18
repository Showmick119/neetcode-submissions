class Solution {
    public boolean isPalindrome(String s) {
        s = s.replaceAll("[^a-zA-Z0-9]", "");
        int L = 0;
        int R = 0;
        while (L < R) {
            if (s.charAt(L) != s.charAt(R)) {
                return false;
            }
            L++;
            R--;
        }
        return true;
    }
}
