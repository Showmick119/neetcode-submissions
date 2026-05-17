class Solution {
    public int findKthLargest(int[] nums, int k) {
        // look for k elements, n times according to space complexity
        // not kth distinct element, meaning there can be duplicates
        // DON'T SORT, as that trivializes the problem

        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for (int num : nums) {
            pq.offer(num);
        }

        while (pq.size() > k) {
            pq.poll();
        }
        // after while-loop breaks, pq.size() = k
        return pq.peek();
    }
}
