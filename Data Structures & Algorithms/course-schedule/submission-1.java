class Solution {
    Set<Integer> visit = new HashSet<>();
    Map<Integer, List<Integer>> adj = new HashMap<>();

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        // EDGE CASE: prerequisites
        // first initialize and create the adjacency list
        // [a, b] => b is a pre-req for a, and will go inside adjacency list for a
        for (int i = 0; i < numCourses; i++) {
            adj.put(i, new ArrayList<>());
        }
        for (int[] prereq : prerequisites) {
            adj.get(prereq[0]).add(prereq[1]);
        }

        // the courses are labeled from 0 to numCourses - 1, so let's
        // start the recursive dfs with 0
        for (int c = 0; c < numCourses; c++) {
            if (!dfs(c)) {
                return false;
            }
        }
        return true;
    }

    // checking if it's empty
    private boolean dfs(int i) {
        if (visit.contains(i)) {
            return false;
        }
        if (adj.get(i).isEmpty()) {
            return true;
        }
        visit.add(i);
        for (int prereq : adj.get(i)) {
            if (!dfs(prereq)) {
                return false;
            }
        }
        // none of it's pre-reqs returned false. meaning all of it's 
        // pre-reqs are completable. Hence, i itself is also completable
        // thus we can remove it from the list and add it back but now
        // with an empty list as it's value, such that isEmpty() triggers.
        visit.remove(i);
        adj.put(i, new ArrayList<>());
        return true;
    }
}
