def maxSubArray(nums):
    current_max = None
    max_sum = None
    for i in range(len(nums)):
        if current_max is None:
            current_max = nums[i]
            max_sum = current_max
            continue
        if current_max + nums[i] > nums[i]:
            current_max += nums[i]
        else:
            current_max = nums[i]
        if current_max > max_sum:
            max_sum = current_max
    return max_sum

print(maxSubArray([-1,0,-2]))