def containsNearbyDuplicate(nums,k):

    index = {}

    for i,num in enumerate(nums):
        if num not in index:
            index[num] = i
        else:
            if abs(index[num] - i) <=k:
                return True
            else:
                index[num] = i

    return False

print(containsNearbyDuplicate(nums = [1,0,1,1], k = 1))