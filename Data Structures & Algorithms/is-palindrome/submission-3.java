class Solution {
    public boolean isPalindrome(String s) {
        int l = 0;
        int r = s.length() - 1;
        String sClear = s.replaceAll("\\s++", "");
        String small = sClear.toLowerCase();

        while (l < r) {
            if (small.charAt(l) != small.charAt(r)) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
}