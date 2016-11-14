import java.util.*;

public class Solution{

  public int[] plusOne(int[] digits) {

      boolean carry = true;
      for(int i = digits.length - 1;i >= 0;i--) {
          if(carry) {
            int sum = digits[i] + 1;

            /**
            *
            *   加法进位的时候，可以用%10取值，用/10决定是否进位，比sum=10来判断简洁更多
            */

            digits[i] = sum % 10;
            carry = sum / 10 == 1?true:false;
          } else {
              break;
          }
      }

      if(carry) {
          int[] temp = new int[digits.length + 1];
          Arrays.fill(temp,0);
          temp[0] = 1;
          return temp;
      } else {
          return digits;
      }

  }

  public static void main(String[] args) {

      int[] src = {9,9,9,9};

      Solution s = new Solution();
      int[] res = s.plusOne(src);

      for(int i:res) {
        System.out.print(i + ",");
      }
  }
}
