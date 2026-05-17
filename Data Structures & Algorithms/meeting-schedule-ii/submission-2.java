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

        if (intervals.size() == 0) {
            return 0;
        }
        if (intervals.size() == 1) {
            return 1;
        }
        
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();

        for (Interval interval : intervals) {
            if (!minHeap.isEmpty() && minHeap.peek() <= interval.start) {
                /*
                Removing such that another element of the same day can
                be added, and the size of the heap still stays minimal
                and indicates that they were all on the same day. Hence,
                size of heap didn't increase, and rather stayed the same,
                since all these meetings were happening on the same day,
                and we want the size of the heap to indicate how many
                days it takes.

                Day N : ____ last meeting time
                Day N + 1: ___ last meeting time

                - Don't poll when they are in different times. Such that
                the size of heap can increase, and indicate that the 
                meetings are indeed on different days, and increasing
                the total number of days needed to complete all the meetings.
                */
                minHeap.poll();
            }
            // Will always at least be 1 day
            minHeap.offer(interval.end);
        }
        return minHeap.size();
    }
}

/*
- (0,8),(8,10) is not considered a conflict at 8.
- Everytime we have a conflict, we increment the day by 1.
- Not necessarily sorted. So must sort on our own at the start.
- We are taking the scenario that a person can end a meeting and 
immediately at the same time, start another meeting.
*/