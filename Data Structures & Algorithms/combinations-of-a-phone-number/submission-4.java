class Solution {
    private String[] map = {
            "", "", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", 
            "WXYZ"
    };

    public List<String> letterCombinations(String digits) {
        List<String> combos = new ArrayList<>();
        helper(0, new StringBuilder(), digits, combos);
        return combos;
    }

    private void helper(int i, StringBuilder s, String digits, List<String> combos) {
        if (i >= digits.length() || s.length() == digits.length()) {
            // further changes to StringBuilder will not affect this
            // s.toString(), since that has created a new immutable
            // String
            combos.add(s.toString());
            return;
        }

        int index = digits.charAt(i) - '0';
        String letter = map[index];

        for (char c : letter.toCharArray()) {
            s.append(c);
            helper(i + 1, s, digits, combos);
            s.deleteCharAt(s.length() - 1);
        }
    }
}
