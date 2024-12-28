# def rotateArray(nums,k):
#     for i in range(k):
#         nums.insert(0,nums[-1])
#         nums.pop()
#     return nums


# def rotateArray(nums,k):
#     n = len(nums)
#     result = [0]*n
#     k = k%n
#     for i in range(len(nums)):
#         result[(i+k)%n] = nums[i]
#     for i in range(len(nums)):
#         nums[i] = result[i]

# def rotateArray(nums,k):
#     k = k%len(nums)
#     if k!=0:
#         nums[:k],nums[k:] = nums[-k:],nums[:-k]
#     return nums

# def rotateArray(nums,k):
#     k%=len(nums)
#     def reverse(left,right):
#         while left < right:
#             nums[left],nums[right] = nums[right],nums[left]
#             left+=1
#             right-=1
#     reverse(0,len(nums)-1)
#     reverse(0,k-1)
#     reverse(k,len(nums)-1)













def rotateArray(nums,k):
    n = len(nums)
    k%=n
    nums[0:k],nums[k:n] = nums[k:n],nums[0:k]
    return nums
print(rotateArray([-1,-100,3,99],2))