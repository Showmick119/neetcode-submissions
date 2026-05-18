class Solution {
    public boolean validTree(int n, int[][] edges) {
        if (edges.length == 0) {
            return true; // empty tree is
        }
        Map<Integer, List<Integer>> map = new HashMap<>();
        Set<Integer> set = new HashSet<>();

        for (int i = 0; i < n; i++) {
            map.put(i, new ArrayList<>());
        }

        for (int[] edge : edges) {
            map.get(edge[0]).add(edge[1]);
            map.get(edge[1]).add(edge[0]);
        }

        if (!dfs(0, -1, visit, map)) {
            return false;
        }

        return visit.size() == n;
    }

    private void dfs(int node, int parent, Set<Integer> visit, List<List<Integer>> map) {
        if (visit.contains(node)) {
            return false;
        }

        visit.add(node);
        for (int neighbor : map.get(node)) {
            if (neighbor == parent) {
                continue; // can't go to parent, and we might since it's undirected
            }
            if (!dfs(neighbor, node, visit, map)) {
                return false;
            }
        }
        return true;
    }
}
