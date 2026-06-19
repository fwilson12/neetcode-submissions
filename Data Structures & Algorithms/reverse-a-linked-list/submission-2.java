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
        
        // init pointers
        ListNode prev = null;
        ListNode curr = head;
        // curr will end up null, so prev will be last elem
        while (curr != null) {
            // need ptr to next elem for next iteration
            ListNode next = curr.next;
            // relink curr to prev
            curr.next = prev;
            // inc pointers
            prev = curr;
            curr = next;
        }
        return prev;

    }
}
