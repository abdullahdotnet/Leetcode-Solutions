def summaryRanges(nums):
    result = []
    if nums:
        res = f"{nums[0]}"
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] == 1:
                pass
            else:
                if int(res)!= nums[i]:
                    res+=f"->{nums[i]}"
                result.append(res)
                res = f"{nums[i+1]}"
        if nums[-1] != int(res):
            result.append(f"{res}->{nums[-1]}")
        else:
            result.append(res)
    return result