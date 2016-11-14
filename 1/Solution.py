def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # this is O(n^2logn)
    # for i in range(len(nums)):
    #     other = target - nums[i]
    #     # don't forget the same number
    #     if (other) in nums and nums.index(other) != i :
    #         return [i,nums.index(other)]
    dist = {}
    for i in range(len(nums)):
        if nums[i] not in dist:
            dist[nums[i]] = [i]
        else:
            dist[nums[i]].append(i)

    for i in range(len(nums)):
        another = target - nums[i]
        if another in dist:
            anotherIndex = dist[another]
            if len(anotherIndex) == 1 and anotherIndex[0] != i:
                return [i,anotherIndex[0]]
            if len(anotherIndex) == 2:
                return [i,anotherIndex[1]]



print(twoSum([0,4,3,0],0))
