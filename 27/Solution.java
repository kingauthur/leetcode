/**
*  解题注意点：
*  这种题目一开始就要考虑2个指针。既然是两个指针，就要想到可能会有交换，然而这个有一个很关键的隐藏信息，就是超过长度以后的数据根本不care，所以没有直接覆盖就好
*
*/

public class Solution{

  public int removeElement(int[] nums, int val) {

      int i = 0,j = 0;

      while(j < nums.length) {
        if(nums[j] != val) {
          nums[i] = nums[j];
          i++;
        }
        j++;
      }

      return i;
  }

  public static void main(String[] args) {

      int[] src = {1,2,3,4};

      Solution s = new Solution();
      System.out.println("length: " + s.removeElement(src,2));
      for(int i:src) {
        System.out.print(i + ",");
      }
  }
}
