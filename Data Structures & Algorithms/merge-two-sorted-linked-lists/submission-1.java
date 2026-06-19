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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        
        ListNode curr1 = list1;
        ListNode curr2 = list2;

        if (list1 == null && list2 == null) {
            return null;
        }
        else if (list1 == null) {
            return list2;
        }
        else if (list2 == null) {
            return list1;
        }


        ListNode currRes = null;
        if (curr1.val < curr2.val) {
            currRes = curr1;
            curr1 = curr1.next;
        } else {
            currRes = curr2;
            curr2 = curr2.next;
        }
        ListNode resHead = currRes;

        while (!(curr1 == null || curr2 == null)) {
            if (curr1.val < curr2.val) {
                currRes.next = curr1;
                curr1 = curr1.next;
                currRes = currRes.next;
            } else {
                currRes.next = curr2;
                curr2 = curr2.next;
                currRes = currRes.next;

            }
        }

        while (curr1 != null) {
            currRes.next = curr1;
            curr1 = curr1.next;
            currRes = currRes.next;
        }
        while (curr2 != null) {
            currRes.next = curr2;
            curr2 = curr2.next;
            currRes = currRes.next;
        }

        return resHead;


    }
}