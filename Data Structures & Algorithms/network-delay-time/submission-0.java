class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        // Can do it all in one method. No need for helper methods.
        // First build the adjacency list.
        Map<Integer, List<int[]>> adj = new HashMap<>();
        for (int i = 1; i < n + 1; i++) {
            adj.put(i, new ArrayList<int[]>());
        }
        // List of arrays, where each array indicates a destination
        // node and the distance to it.
        for (int[] time : times) {
            adj.get(time[0]).add(new int[]{time[1], time[2]});
        }
        
        PriorityQueue<int[]> minHeap = new PriorityQueue<>(
            Comparator.comparing(a -> a[1])
        );

        // k is the Node we will send the signal from. So the distance
        // to this Node is 0.
        minHeap.offer(new int[]{k, 0});

        Set<Integer> visited = new HashSet<>();
        int total = 0;
        while (!minHeap.isEmpty()) {
            int[] curr = minHeap.poll();
            int n1 = curr[0], time1 = curr[1];
            if (visited.contains(n1)) {
                continue;
            }
            visited.add(n1);
            // No need for incrememnt, as the increment will happen before adding to minHeap
            total = time1; // will give us max time

            if (adj.containsKey(n1)) {
                for (int[] neighbor : adj.get(n1)) {
                    int n2 = neighbor[0], time2 = neighbor[1];
                    if (!visited.contains(n2)) {
                        minHeap.offer(new int[]{n2, time1 + time2});
                    }
                }
            }
        }

        // have to check if all the Nodes have been visited
        if (visited.size() == n) {
            return total;
        } else {
            return -1;
        }
    }
}
