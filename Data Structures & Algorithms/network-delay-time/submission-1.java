class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        int total = 0;
        Map<Integer, List<int[]>> map = new HashMap<>();
        Map<Integer, Integer> minDist = new HashMap<>();
        for (int i = 1; i <= n; i++) {
            map.put(i, new ArrayList<>());
        }
        for (int[] edge : times) {
            map.get(edge[0]).add(new int[]{edge[1], edge[2]});
        }
        // minHeap of all the nodes and time it takes to get to them
        // the cumulative timee
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparing(a -> a[1]));
        pq.add(new int[]{k, 0}); // adding the source node and the time to it
        Set<Integer> visit = new HashSet<>();
        while (!pq.isEmpty() && visit.size() != n) {
            int[] curr = pq.poll();
            minDist.put(curr[0], curr[1]);
            if (!visit.contains(curr[0])) {
                visit.add(curr[0]);
                total = curr[1];
                for (int[] neighbor : map.get(curr[0])) {
                    pq.add(new int[]{neighbor[0], neighbor[1] + curr[1]});
                }
            }
        }

        if (visit.size() != n) {
            return -1;
        } else {
            return total;
        }
    }
}