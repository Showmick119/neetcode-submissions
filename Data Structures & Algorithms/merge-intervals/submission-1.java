class Solution {
    public int[][] merge(int[][] intervals) {
        // We will sort it by the starting index
        // Need O(nlogn) due to the sorting algorithm
        Arrays.sort(intervals, Comparator.comparing(a -> a[0]));
        // can also use comparingInt() for efficiency
        
        List<int[]> indices = new ArrayList<>();
        int prevStart = intervals[0][0], prevEnd = intervals[0][1];

        for (int i = 1; i < intervals.length; i++) {
            int currStart = intervals[i][0], currEnd = intervals[i][1];
            if (currStart <= prevEnd) {
                // overlapping
                prevEnd = Math.max(prevEnd, currEnd); // updating end
            } else {
                // non-overlapping
                // just cause 1st and 2nd interval aren't overlapping, doesn't
                // mean that 2nd and interval can't be overlapping. So only
                // add the prev interval, as that has been cleared.
                indices.add(new int[]{prevStart, prevEnd});
                
                // start tracking the new interval
                // The currStart is greater than the prevEnd, so we are
                // no longer overlapping! So we start tracking a new set
                // as well as it's start and end values!
                prevStart = currStart;
                prevEnd = currEnd;
            }
            // prevStart = currStart;
            // prevEnd = currEnd;
        }
        indices.add(new int[]{prevStart, prevEnd});

        int[][] output = new int[indices.size()][2];
        for (int i = 0; i < output.length; i++) {
            int[] indice = indices.get(i);
            output[i][0] = indice[0];
            output[i][1] = indice[1];
        }
        return output;
    }
}

/*
O(1) > O(logn) > O(n) > O(nlogn) > O(n^2) > O(2^n)
*/