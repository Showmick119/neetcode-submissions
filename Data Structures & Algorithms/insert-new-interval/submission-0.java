class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        // Edge Case 1:
        if (intervals.length == 0) {
            return new int[][]{{newInterval[0], newInterval[1]}};
        }
        int newStart = newInterval[0], newEnd = newInterval[1];
        List<int[]> newIntervals = new ArrayList<>();
        boolean added = false;

        // 1st Loop: Inserting the new interval
        for (int i = 0; i < intervals.length; i++) {
            int currStart = intervals[i][0], currEnd = intervals[i][1];
            if (newStart <= currStart) {
                newIntervals.add(new int[]{newStart, newEnd});
                added = true;
            }
            newIntervals.add(new int[]{currStart, currEnd});
        }
        if (!added) {
            newIntervals.add(new int[]{newStart, newEnd});
        }

        List<int[]> indices = new ArrayList<>();
        int currStart = newIntervals.get(0)[0];
        int currEnd = newIntervals.get(0)[1];
        // 2nd Loop: Merging any potential overlaps, after the insertion
        for (int i = 1; i < newIntervals.size(); i++) {
            if (newIntervals.get(i)[0] <= currEnd) {
                currEnd = Math.max(currEnd, newIntervals.get(i)[1]);
            } else {
                indices.add(new int[]{currStart, currEnd});
                currStart = newIntervals.get(i)[0];
                currEnd = newIntervals.get(i)[1];
            }
        }
        indices.add(new int[]{currStart, currEnd});

        int[][] output = new int[indices.size()][2];
        for (int i = 0; i < output.length; i++) {
            output[i][0] = indices.get(i)[0];
            output[i][1] = indices.get(i)[1];
        }
        return output;
    }
}

/*
Imagine it just like the merge intervals. But now you also
have to figure out where to exactly place the newInterval.
*/