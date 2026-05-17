class Solution {
    public int[][] kClosest(int[][] points, int k) {
        // create a special heap? WHICH WILL AUTO-SORT MIN BY A SPECIFIC POINT
        // don't just return THE shortest path element, have to return 
        // the shortest k elements
        // not using sqrt() allows us to simplify and use int
        // since we are substracing with origin (0, 0), we have to substract
        // by 0 anyways. And then a - 0 = a, so you might as well do a * a from the start.
        // (a -> a[0]): given an Array a, sort by the first element, which in our case is distance
        // that's the array we will pass to the priority queue with offer()
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparing(a -> a[0]));

        for (int[] point : points) {
            int dist = point[0] * point[0] + point[1] * point[1];
            pq.offer(new int[]{dist, point[0], point[1]});
        }

        int[][] closest = new int[k][2]; // k rows of pairs (2)
        for (int i = 0; i < k; i++) {
            int[] temp = pq.poll();
            closest[i][0] = temp[1];
            closest[i][1] = temp[2];
        }
        return closest;
    }
}
