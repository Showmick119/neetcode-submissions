class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

        for (int stone : stones) {
            pq.offer(stone); // add() and remove() can throw exceptions
            // poll() and offer() are safer operations
        }

        while (pq.size() > 1) {
            int x = pq.poll(); // already removing from Heap (so kind of destorying)
            int y = pq.poll();
            if (x > y) {  // minHeap will add it back to it's relevant position automatically
                pq.offer(x - y);
            }
        }

        if (pq.isEmpty()) {
            return 0;
        } else {
            return pq.peek(); // didn't say to remove it, so don't do extra step with poll()
        }
    }
}
