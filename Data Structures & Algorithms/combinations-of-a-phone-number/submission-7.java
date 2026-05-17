class Solution {
    private String[] map = {
            "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", 
            "wxyz"
    };

    public List<String> letterCombinations(String digits) {
        if (digits.length() == 0) {
            // edge case that what if digits length is 0
            // it is mentioned in our constraints that digits.length can
            // be 0, so have to take care of that edge case
            return new ArrayList<>();
        }
        List<String> combos = new ArrayList<>();
        helper(0, new StringBuilder(), digits, combos);
        return combos;
    }

    private void helper(int i, StringBuilder s, String digits, List<String> combos) {
        if (i >= digits.length()) {
            // further changes to StringBuilder will not affect this
            // s.toString(), since that has created a new immutable
            // String
            combos.add(s.toString());
            return;
        }

        int index = digits.charAt(i) - '0';

        if (index < 2 || index > 9) {
            return;
        }
        String letter = map[index];

        for (char c : letter.toCharArray()) {
            s.append(c);
            helper(i + 1, s, digits, combos);
            s.deleteCharAt(s.length() - 1);
        }
    }
}
