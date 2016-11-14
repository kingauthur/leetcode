def findKthElement(nums1,nums2,k):
    if len(nums1) > len(nums2):
        return findKthElement(nums2,nums1,k)
    if len(nums1) == 0:
        return nums2[k-1]
    if k == 1:
        return min(nums1[0],nums2[0])

    point1 = min(len(nums1),k/2)
    point2 = k - point1

    if nums1[point1-1] < nums2[point2-1]:
        return findKthElement(nums1[point1:len(nums1)],nums2,k - point1);
    elif nums1[point1-1] > nums2[point2-1]:
        return findKthElement(nums1,nums2[point2:len(nums2)],k - point2);
    else:
        return nums1[point1-1];




def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    total = len(nums1) + len(nums2)
    if total % 2  == 1:
        return findKthElement(nums1,nums2,total/2 + 1)
    else:
        left = findKthElement(nums1,nums2,total/2)
        right = findKthElement(nums1,nums2,total/2 + 1)
        return (left + right) * 1.0 / 2

nums1 = [1, 2]
nums2 = [3, 4]
print(findMedianSortedArrays(nums1,nums2))
