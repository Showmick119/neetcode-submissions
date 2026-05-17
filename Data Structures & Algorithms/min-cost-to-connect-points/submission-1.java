class Solution {
    public int minCostConnectPoints(int[][] points) {
        // Applying Prim's algorithm, which doesn't use Union-Find
        // like Kruskal's algorithm.
        // First create the adjacency list from the 2D array of points.
        // Here we don't have a single integer value to store as nodes.
        // Rather we have proper points with (x, y) coordinates.
        // We're going to refer to each point in the list as the index
        // of that point.
        // For every single point, we want to compare it to every other
        // point in the graph.
        
        int N = points.length;

        // For each Node, we are mapping it to a list of POINTS (x, y).
        // For each point, we're going to have the cost and the neighbor.
        // Each neighbor is a pair. As each edge, is a weighted edge.
        Map<Integer, List<int[]>> adj = new HashMap<>();

        for (int i = 0; i < N; i++) {
            adj.put(i, new ArrayList<>());
        }
        // Big thing is that we are given arrays, and we need to store
        // them as Nodes. And we will store them as Nodes through indexes.
        // It's still a graph in the end of the day.
        for (int i = 0; i < N; i++) {
            int x1 = points[i][0], y1 = points[i][1];
            for (int j = i + 1; j < N; j++) {
                int x2 = points[j][0], y2 = points[j][1];
                // Now that we have two points. We will calculate the
                // Manhattan distance between them.
                int dist = Math.abs(x1 - x2) + Math.abs(y1 - y2);
                // Remember that even though we have points, we are
                // taking the index to be the representative of the Node.
                // The edges are undirected.
                adj.get(i).add(new int[]{dist, j});
                adj.get(j).add(new int[]{dist, i});
            } 
        }

        // Prim's Algorithm
        int res = 0;
        Set<Integer> visit = new HashSet<>();
        PriorityQueue<int[]> minHeap = new PriorityQueue<>(
            Comparator.comparing(a -> a[0])
        );
        // Connecting all points together, but not creating a cycle. 
        // Hence, keeping the Tree definition.
        // Starting off with index 0 (Node 0), point
        minHeap.offer(new int[]{0, 0}); // each pair will be the cost and point

        while (visit.size() < N) { // stop when we have added all N nodes
            int[] curr = minHeap.poll();  // pop and then add it's neighbors
            int cost = curr[0], point = curr[1];
            // If that node/point has already been visited, we will
            // skip over this iteration.
            if (visit.contains(point)) {
                continue; // want to skips Node's we've already visited.
            }
            res += cost; // we aren't actually 'building' a tree. We are just visiting it and adding it's cost to our final output.
            visit.add(point); // not adding neighbors, only adding points which have been properly visited via shortest path.
            // Then we go through all the neighbors of point.
            for (int[] neighbor : adj.get(point)) {
                int neighborCost = neighbor[0];
                int neighborPoint = neighbor[1];
                if (!visit.contains(neighborPoint)) { // will add all the ones which are yet to be visited
                    // Remember that it's undirected. So in this neighbor
                    // node's list, it also has the parent node (the current node
                    // from which it all came). But since the parent node
                    // has already been added (it's cost) and is part of
                    // the MST. We will not be cycling back to it.

                    // We will add all the paths, distances to a Node, to our Heap.
                    // But we will only take and use the shortest one.

                    // We will only add Nodes which have not been visited
                    // at all, and it's neighbors haven't been processed.

                    minHeap.offer(new int[]{neighborCost, neighborPoint});
                    // We need duplicates, as we need to know the different
                    // ways a Node can be reached. Such that we can find
                    // the shortest one.

                    // The min Heap will have more elements than we need, and that is okay,
                    // as we just need to get the one with the shortest path.
                }
            }
        }
        return res;
    }
}
