public class Solution{

  public String reverseString(String s){

    // ---------------soluition 1--------------
    // int range = s.length() - 1;
    // char[] result = new char[s.length()];
    //
    // for(int left = 0;left <= s.length()/2; left++) {
    //     int right = range - left;
    //
    //     if (left < right) {
    //       result[left] = s.charAt(right);
    //       result[right] = s.charAt(left);
    //     }
    //     else if (left == right) {
    //       result[left] = s.charAt(left);
    //     } else {
    //       break;
    //     }
    // }
    //
    // return String.valueOf(result);


    //---------------solution 2-----------------
    StringBuilder sb = new StringBuilder();
    for(int index = (s.length() - 1); index >= 0 ; index--) {
      sb.append(s.charAt(index));
    }
    return sb.toString();
  }

  public static void main(String[] args) {
    Solution solution = new Solution();
    System.out.println(solution.reverseString("hello"));
  }
}
