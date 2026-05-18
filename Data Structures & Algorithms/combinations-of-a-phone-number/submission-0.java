class Solution {
    List<String> res = new ArrayList<>();
    String[] map = {
        "", "", "abc", "def", "ghi", "jkl", "mno", "qprs",
        "tuv", "wxyz"
        };
    public List<String> letterCombinations(String digits) {
        if (digits.length() == 0) {
            return res;
        }
        backtrack(0, digits, new StringBuilder());
        return res;
    }

    private void backtrack(int i, String digits, StringBuilder curr) {
        if (curr.length() == digits.length()) {
            res.add(curr);
            return;
            // all Strings of the list will be same length as original
        }

        int index = digits.charAt(i) - '0';
        String letters = map[index];

        for (char c : letters.toCharArray()) {
            curr.append(c);
            backtrack(i + 1, digits, curr);
            curr.deleteCharAt(curr.length() - 1);
        }
    }
}
