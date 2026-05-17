class Solution {
    public boolean isPalindrome(String s) {
        s = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        StringBuilder sb1 = new StringBuilder(s);
        sb1.reverse();
        String s1 = sb1.toString();
        if (s.equals(s1)) {
            return true;
        } else {
            return false;
        }
    }
}
