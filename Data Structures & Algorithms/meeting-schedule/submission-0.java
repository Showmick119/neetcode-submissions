/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public boolean canAttendMeetings(List<Interval> intervals) {
        // Edge Case 1: What if there are no meetings at all?
        if (intervals.size() == 0) {
            return true;
        }
        Collections.sort(intervals, Comparator.comparingInt(a -> a.start));
        int currStart = intervals.get(0).start;
        int currEnd = intervals.get(0).end;
        for (int i = 1; i < intervals.size(); i++) {
            if (intervals.get(i).start <= currEnd) {
                return false;
            }
            currStart = intervals.get(i).start;
            currEnd = intervals.get(i).end;
        }
        return true;
    }
}
