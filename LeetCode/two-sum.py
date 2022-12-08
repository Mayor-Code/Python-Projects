def twoSum(nums, target):
    index1 = 0
    while index1 < (len(nums)-1):
        index2 = index1 + 1
        while index2 < len(nums):
            if nums[index1] + nums[index2] == target:
                return [index1, index2]
            index2 += 1
        index1 += 1
    return []




print(twoSum([3,2,4],6))