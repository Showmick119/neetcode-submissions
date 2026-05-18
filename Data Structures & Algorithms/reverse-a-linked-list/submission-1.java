/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode move = head;
        ListNode next;
        while (move.next != null) {
            if (move == head) {
                next = move.next;  // store the next element of the head
                next.next = move;  // make the next element of the head point to the head
                ListNode oldHead = move;
                move.next = null;  // make head's next point to null
            } else {
                next = move.next;
                next.next = move;
            }
            move = move.next;
        }
        next = move.next;
        next.next = move;
        head = move;
        return head;
    }
}
