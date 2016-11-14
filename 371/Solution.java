public class Solution{
  public int getSum(int a, int b) {
    if(b == 0) {
      return a;
    }
    int sum = a ^ b;
    int carry = (a & b) << 1;

    return getSum(sum, carry);
  }
  public static void main(String[] args) {
    Solution s = new Solution();
    System.out.println(s.getSum(11,13));
  }
}
