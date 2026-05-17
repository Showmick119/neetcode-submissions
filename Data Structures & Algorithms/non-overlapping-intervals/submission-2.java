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
                // We want to find the MINIMUM amount of intervals we
                // need to remove to make it not overlapping.
                // So taking the max which will keep sucking up the 
                // other intervals is not the correct greedy strategy.
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

/*
When two intervals overlap, keep the one with the earlier end time 
because it leaves more space for future intervals.

Example: [[1,4], [2,3], [3,5]]
- If we go with the maximum strategy, our final intervals would be
[[1, 5]]. But we don't need to remove 2 intervals to make it non
overlappng.
- How about we remove [1, 4], it is overlapping now? No, now the
intervals are non-overlapping.
- So we can remove from either end, point is that we want to remove the
minimum possible.
- So take the minimum endTime, such that we can get less overlapping
intervals in the future. We are still taking overlaps, but we are now
optimally removing from either direction, to make sure that, whatever
remains, is the maximum possible, and that we removed as little as
possible.

- [1,4] and [2,3] overlap
- Keep [2,3] (ends earlier), remove [1,4]
- [2,3] and [3,5] don't overlap (touching is OK)

Result: Remove 1 interval
*/
