public class Solution {

    public void merge(int[] nums1, int m, int[] nums2, int n) {
      // TODO 关注下答案排序的顺序重要与否
      // Answer: 排序默认都是从小到大的
      int lastIndexOfNum1 = m - 1;
      int lastIndexOfNum2 = n - 1;
      int lastIndex = m + n - 1;
      while (lastIndexOfNum1 >= 0 && lastIndexOfNum2 >= 0) {
          if(nums1[lastIndexOfNum1] >= nums2[lastIndexOfNum2]) {
            nums1[lastIndex--] = nums1[lastIndexOfNum1--];
          } else {
            nums1[lastIndex--] = nums2[lastIndexOfNum2--];
          }
      }

      while (lastIndexOfNum1 >= 0) {
        nums1[lastIndex--] = nums1[lastIndexOfNum1--];
      }

      while (lastIndexOfNum2 >= 0) {
        nums1[lastIndex--] = nums2[lastIndexOfNum2--];
      }

    }

}
