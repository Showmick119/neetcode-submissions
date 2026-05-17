class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        Map<Integer, List<int[]>> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            map.put(i, new ArrayList<>());
        }
        for (int[] flight : flights) {
            map.get(flight[0]).add(new int[]{flight[1], flight[2]});
        }
        boolean reached = false;
        int cheapest = 100000000;
        List<Integer> minList = new ArrayList<>();
        Set<Integer> set = new HashSet<>();
        PriorityQueue<int[]> pq = new PriorityQueue<>(
            Comparator.comparing(a -> a[1])
        ); // [dst, cost, stopNumber]
        // when we start with 0 we are essentially not counting the starting edge
        // when we minus again, we are essentially not counting the ending edge
        // with these two minuses we are cutting out starting and ending, and only keeping
        // the intermediate airports. now if we start with -1 instead of 0, then
        // we are skipping both the starting the ending vertices subconciously.
        pq.add(new int[]{src, 0, -1});
        // you don't increment stops for the src and dst nodes
        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int airport = curr[0]; int cost = curr[1]; int stops = curr[2];
            if (airport == dst) {
                if (stops <= k) {
                    reached = true;
                    if (cost < cheapest) {
                        cheapest = cost;
                        return cheapest;
                    }
                }
            }
            for (int[] neighbor : map.get(curr[0])) {
                if (stops <= k && (neighbor[1] + cost) < cheapest) {
                    pq.add(new int[]{neighbor[0], neighbor[1] + cost, stops + 1});
                }
            }
        }
        if (!reached) {
            return -1;
        } else {
            return cheapest;
        }
    }
}