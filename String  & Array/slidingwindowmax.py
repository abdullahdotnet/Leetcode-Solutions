def maxSlidingWindow(nums,k):
    i = 0
    result = []
    if len(nums) <= k:
        result.append(max(nums))
        return result
    while i+k <= len(nums):
        result.append(max(nums[i:i+k]))
        i+=1
    return result

print(maxSlidingWindow([1],1))
