class KthLargest {
    int k;
    PriorityQueue<Integer> minHeap = new PriorityQueue<>();

    /*
    - Our Min Heap will be of size k.
    - offer() and poll() are add and remove operations of O(log(n)).
    - Accesing minimum element is O(1).
    - While size of Heap is greater than k, we will pop the minimum value.
    - Now when we do heap.poll() we will get the kth largest element.
    - Cause in a MinHeap of size k, the smallest element is the kth largest element.
    */

    public KthLargest(int k, int[] nums) {
        this.minHeap = minHeap;
        this.k = k;

        for (int num : nums) {
            minHeap.offer(num);
        }

        while (minHeap.size() > k) { // ensures heap is off size k
            minHeap.poll();
        }
    }
    
    // Each add is an O(log(n)) operation. For m elements, the Big-O
    // would be a total of O(m * log(n)).
    public int add(int val) {
        // add val and return Kth largest element
        // whenever we call this function, we are guaranteed to have
        // at least k elements in the Stream of data
        minHeap.offer(val);

        if (minHeap.size() > k) { // larger due to the ADDITION OF VAL, since we initially get it at size k
            minHeap.poll(); // can remove since there's more than k elements
        }
        
        // WE ARE ASSUMING THAT IT'S GUARANTEED TO HAVE AT LEAST k NUMBERS
        // in the stream, when asking for kth largest.

        // only remove IF there's less than k elements
        return minHeap.peek(); // size is still within k, so we can return the kth largest element
        // there must always be k integers in the stream
    }
}
