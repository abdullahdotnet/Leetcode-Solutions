def BinarSearch(nums,n):
    left = nums[0]
    right = nums[-1]
    mid = (left+right)/2
    while left < right:
        if mid == n:
            return True
        elif mid > n:
            right = mid
        elif mid < n:
            left = mid
    return False


BinarSearch([1,2,2,4,6,7,8,12,14,15],12)