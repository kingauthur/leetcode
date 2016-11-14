/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
import java.util.*;

public class Solution {
    public ListNode mergeKLists(ListNode[] lists) {

        if(lists == null || lists.length == 0) {
            return null;
        } else if(lists.length == 1) {
            return lists[0];
        } else {
            ListNode[] newList = mergeLastTwo(lists);
            return mergeKLists(newList);
        }

    }

    public ListNode[] mergeLastTwo(ListNode[] lists) {
        List<ListNode> toLists = new ArrayList<ListNode>(Arrays.asList(lists));
        ListNode lastOne = toLists.get(toLists.size() - 1);
        ListNode lastTwo = toLists.get(toLists.size() - 2);
        ListNode sorted = merge(lastOne,lastTwo);
        toLists.remove(toLists.size() - 1);
        toLists.remove(toLists.size() - 2);
        toLists.add(sorted);
        return (ListNode[])toLists.toArray();
    }


    public ListNode merge(ListNode first, ListNode second) {
        return null;
    }

    public int headValue(ListNode list) {
        return list.val;
    }

    public int tailValue(ListNode list) {
        ListNode temp = list;

        while(temp.next != null)  {
            temp = temp.next;
        }

        return temp.val;
    }

}



class ListNode {
     int val;
     ListNode next;
     ListNode(int x) { val = x; }
 }
