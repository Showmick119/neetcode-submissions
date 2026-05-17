class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparing(a -> a[0]));
        // Edge Case: what if intervals.length == 1?
        if (intervals.length == 1) {
            return 0;
        }
        // The element we are processing, and will only add once we
        // are done processing it, and have it's start and end indices
        // finalized.
        int currStart = intervals[0][0], currEnd = intervals[0][1];
        int count = 0;

        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] < currEnd) {
                currEnd = Math.min(currEnd, intervals[i][1]);
                count++;
            } else {
                currStart = intervals[i][0];
                currEnd = intervals[i][1];
            }
        }
        return count;
    }
}
