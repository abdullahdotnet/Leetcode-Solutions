def plusOne(digits):
    # 1st Approach
    num = int(''.join(map(str,digits)))
    num+=1
    return [int(digit) for digit in str(num)]

    # 2nd Approach
    # return list(map(int,(str(int(''.join(map(str, digits))) + 1))))

    # 3rd Approach
    
    # num = 0
    # for digit in digits:
    #     num = num * 10 + digit
    # num += 1
    # return [int(digit) for digit in str(num)]

print(plusOne([9]))