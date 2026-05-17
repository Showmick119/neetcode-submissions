class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> sub = new HashSet<Character>();
        int L = 0;
        int maxLength = 0;
        
        for (int R = 0; R < s.length(); R++) {
            while (sub.contains(s.charAt(R))) {
                sub.remove(s.charAt(L));
                L++;
                maxLength = Math.max(maxLength, (R - L + 1));
            }
            sub.add(s.charAt(R));
            maxLength = Math.max(maxLength, (R - L + 1));
        }
        return maxLength;
    }
}
