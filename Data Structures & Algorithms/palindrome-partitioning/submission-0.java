class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> pals = new ArrayList<>();
        List<String> currPal = new ArrayList<>();
        helper(0, s, currPal, pals);
        return pals;
    }

    /* What are the decisions we need to make?
    - What are the extremes?
    - Empty String is NOT a substring of the main String.
    -    
    */

    private void helper(int i, String s, List<String> currPal, List<List<String>> pals) {
        if (i >= s.length()) {
            pals.add(new ArrayList<>(currPal));
            return;
        }

        for (int j = i; j < s.length(); j++) {
            if (isPali(s, i, j)) {
                currPal.add(s.substring(i, j + 1)); // excludes j + 1 to get j
                helper(j + 1, s, currPal, pals);
                currPal.remove(currPal.size() - 1);
            }
        }
    }

    private boolean isPali(String s, int i, int j) {
        int l = i;
        int r = j;

        while (l < r) {
            if (s.charAt(l) != s.charAt(r)) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
}