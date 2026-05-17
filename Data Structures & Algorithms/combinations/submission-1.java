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
            /*
            currComb is still there and has as many elements as it
            did before. If it was [1, 2] before, currComb is still [1, 2]
            even after this base case is hit. What really happened is that
            a deep copy was made of the currComb and added to the combs list.
            Now, even when we make changes to currComb, the one passed into
            combs list is going to be unchanged and untouched, since that
            is a different Object with a different reference, as we used
            the new keyword.
            */
            return;
        }

        if (i > n) {
            return;
        }

        // Include i
        currComb.add(i);
        helper(i + 1, currComb, combs, n, k);

        // Exclude i (the backtracking step)
        currComb.remove(currComb.size() - 1);
        helper(i + 1, currComb, combs, n, k);
    }
}