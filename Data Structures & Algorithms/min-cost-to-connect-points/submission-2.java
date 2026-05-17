class Solution {
    public int minCostConnectPoints(int[][] points) {
        int n = points.length; int m = points[0].length;
        Set<Integer> visit = new HashSet<>();
        Set<int[]> mst = new HashSet<>();
        PriorityQueue<int[]> pq = new PriorityQueue<>(
            Comparator.comparing(a -> a[2])
        ); // [point1, point2, distance]
        // taking 0th index as our starting 
        visit.add(0);
        for (int i = 1; i < n; i++) {
            int x1 = points[0][0];
            int y1 = points[0][1];
            int x2 = points[i][0];
            int y2 = points[i][1];
            int distance = Math.abs(x1 - x2) + Math.abs(y1 - y2);
            pq.add(new int[]{0, i, distance});
        }
        int cost = 0;
        while (!pq.isEmpty() && visit.size() != n) {
            int[] curr = pq.poll();
            if (!visit.contains(curr[1])) {
                visit.add(curr[1]);
                mst.add(new int[]{curr[0], curr[1]}); // [source, target]
                cost += curr[2];
                for (int i = 0; i < n; i++) {
                    if (i != curr[1]) {
                        int x1 = points[curr[1]][0];
                        int y1 = points[curr[1]][1];
                        int x2 = points[i][0];
                        int y2 = points[i][1];
                        int distance = Math.abs(x1 - x2) + Math.abs(y1 - y2);
                        pq.add(new int[]{curr[1], i, distance});
                    }
                }
            }
        }
        return cost;
    }
}