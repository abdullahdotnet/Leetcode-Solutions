# def removeDuplicate(nums):
#     count = 0
#     length = len(nums)
#     i = 0
#     j = 0
#     while i < len(nums):
#         count=0
#         j = i
#         while j < len(nums):
#             if nums[i] == nums[j]:
#                 count+=1
#                 if count > 2:
#                     nums.pop(j)
#                     length-=1
#                     j-=1
#             j+=1
#         i+=1
#     return length


# def removeDuplicate(nums):
#     i = 0
#     j = 1
#     count = 1
#     while i < len(nums) and j < len(nums):
#         if nums[i] == nums[j]:
#             count+=1
#             if count > 2:
#                 nums.pop(j)
#             else:
#                 j+=1
#         else:
#             i = j
#             count = 1
#             if j+1 < len(nums):
#                 j+=1
#             else:
#                 break
#     return len(nums)


def removeDuplicate(nums):
    k = 2

    for i in range(2, len(nums)):
        if nums[i] != nums[k - 2]:
            nums[k] = nums[i]
            k += 1 

    return k
print(removeDuplicate([0,0,1,1,1,1,2,3,3]))
                