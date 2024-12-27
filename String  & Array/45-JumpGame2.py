def jumpGame2(nums):
    near = 0
    far = 0
    jump = 0

    while far < len(nums)-1:
        farthest = 0

        for i in range(near,far+1):
            farthest = max(farthest,i+nums[i])

        near = far+1
        far = farthest
        jump+=1

    return jump
print(jumpGame2([2,3,0,1,4]))