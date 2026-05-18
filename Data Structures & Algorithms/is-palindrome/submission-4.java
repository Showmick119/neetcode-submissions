class Solution {
    public boolean isPalindrome(String s) {
        // use two pointers technique after cleaning up the String
        s = s.replaceAll("\\s+", "");
        char[] arr = s.toCharArray();
        List<Character> cleaned = new ArrayList<>();
        for (char c : arr) {
            if (Character.isLetterOrDigit(c)) {
                cleaned.add(c);
            } else {
                continue;
            }
        }
        char[] cleanedArr = new char[cleaned.size()];
        int i = 0;
        for (char c : cleaned) {
            cleanedArr[i] = c;
            i++;
        }
        StringBuilder sb1 = new StringBuilder(cleanedArr);
        String s1 = sb1.toString().toLowerCase();
        String s2 = sb1.reverse().toString().toLowerCase();
        if (s1.equals(s2)) {
            return true;
        } else {
            return false;
        }
    }
}
