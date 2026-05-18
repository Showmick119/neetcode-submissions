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
    public int minMeetingRooms(List<Interval> intervals) {
        Collections.sort(intervals, Comparator.comparingInt(a -> a.start));
        int days = 1;

        if (intervals.size() == 0) {
            return 0;
        }
        if (intervals.size() == 1) {
            return 1;
        }
        
        int currStart = intervals.get(0).start;
        int currEnd = intervals.get(0).end;

        for (int i = 1; i < intervals.size(); i++) {
            if (intervals.get(i).start < currEnd) {
                days++;
            }
            currStart = intervals.get(i).start;
            currEnd = intervals.get(i).end;
        }
        return days;
    }
}

/*
- (0,8),(8,10) is not considered a conflict at 8.
- Everytime we have a conflict, we increment the day by 1.
- Not necessarily sorted. So must sort on our own at the start.
- We are taking the scenario that a person can end a meeting and 
immediately at the same time, start another meeting.
*/