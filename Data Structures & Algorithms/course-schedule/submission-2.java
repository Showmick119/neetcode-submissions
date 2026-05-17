class Solution {
    Map<Integer, List<Integer>> prereqs = new HashMap<>();
    Set<Integer> visits = new HashSet<>();

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        // It is possible to finish all prereqs if there is no
        // cycle. Meaning you start at a Node and then you end there
        // as well.
        for (int c = 0; c < numCourses; c++) {
            prereqs.put(c, new ArrayList<>());
        }
        for (int[] pre : prerequisites) {
            prereqs.get(pre[0]).add(pre[1]);
        }

        for (int c = 0; c < numCourses; c++) {
            if (!dfs(c)) {
                return false;
            }
        }
        return true;
    }

    private boolean dfs(int c) {
        if (visits.contains(c)) {
            return false; // visiting the same point twice
        }
        if (prereqs.get(c).isEmpty()) {
            return true;
        }
        visits.add(c);

        for (int pre : prereqs.get(c)) {
            if (!dfs(pre)) {
                return false;
            }
        }
        visits.remove(c);
        prereqs.put(c, new ArrayList<>());
        return true;
    }
}
