class Solution {
    Set<Integer> visits = new HashSet<>();
    Set<Integer> cycle = new HashSet<>();
    Map<Integer, List<Integer>> prereqs = new HashMap<>();
    List<Integer> output = new ArrayList<>();

    public int[] findOrder(int numCourses, int[][] prerequisites) {
        for (int i = 0; i < numCourses; i++) {
            prereqs.put(i, new ArrayList<>());
        }
        for (int[] prereq : prerequisites) {
            prereqs.get(prereq[0]).add(prereq[1]);
        }

        for (int i = 0; i < numCourses; i++) {
            if (!dfs(i)) {
                return new int[]{};
            }
        }

        // ONLY START FORMING THE FINAL LIST AFTER THE ENTIRE OUTPUT LIST HAS BEEN CREATED
        int[] order = new int[numCourses];
        for (int i = 0; i < numCourses; i++) {
            order[i] = output.get(i);
        }
        return order;
    }

    private boolean dfs(int i) {
        if (cycle.contains(i)) {
            return false;
        }
        if (visits.contains(i)) {
            return true; // no need to check, already checked its cycle completely
        }
        
        cycle.add(i);
        for (int pre : prereqs.getOrDefault(i, Collections.emptyList())) {
            if (!dfs(pre)) {
                return false;
            }
        }
        cycle.remove(i);
        visits.add(i);
        output.add(i);
        return true;
    }
}
