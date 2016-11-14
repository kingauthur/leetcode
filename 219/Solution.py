def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    #因为题目不需要知道具体的索引
    if len(nums) == len(set(nums)):
    return False
    for i in range(len(nums) - 1):
        subnums = nums[i:(k+i+1 if k+i+1 < len(nums) else len(nums))]
        if len(subnums) != len(set(subnums)):
            # python的boolean第一个字母大写
            return True
    # python的boolean第一个字母大写
    return False


print(containsNearbyDuplicate([4,1,2,3,9,1,5],3))
