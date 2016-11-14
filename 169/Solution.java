import java.util.*;

public class Solution{

  public int majorityElement(int[] nums) {

      Map<Integer,Integer> counter = new HashMap<Integer,Integer>();

      for(int element:nums) {
        if(counter.get(element) == null) {
          counter.put(element,1);
        } else {
          counter.put(element,counter.get(element) + 1);
        }
      }

      for(Map.Entry<Integer,Integer> entry: counter.entrySet()) {
          if(entry.getValue() > nums.length / 2) {
            return entry.getKey();
          }
      }

      return 0;
  }

  1,2,1,1,2,2,1,1

  public static void main(String[] args) {

      int[] src = {1,2,2,2};

      Solution s = new Solution();
      System.out.println("majorityElement: " + s.majorityElement(src));

  }
}
