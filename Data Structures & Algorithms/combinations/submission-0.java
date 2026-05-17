class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> combs = new ArrayList<>();
        List<Integer> currComb = new ArrayList<>();
        // all possible combinations of numbers from 1 to n
        // so 1 must be included as a starting point
        helper(1, currComb, combs, n, k);
        return combs;
    }

    private void helper(int i, List<Integer> currComb, List<List<Integer>> combs, int n, int k) {
        if (currComb.size() == k) {
            combs.add(new ArrayList<>(currComb));
            return;
        }

        if (i > n) {
            return;
        }

        currComb.add(i);
        helper(i + 1, currComb, combs, n, k);
        currComb.remove(currComb.size() - 1);
        helper(i + 1, currComb, combs, n, k);
    }
}