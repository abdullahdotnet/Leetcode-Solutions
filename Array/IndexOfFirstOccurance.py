def indexOfFirstOccurance(heystack,needle):
    j = 0 
    count = 0
    for i in range(len(heystack)+1):
        if j < len(needle):
            if heystack[i] == needle[j]:
                count+=1
                j+=1
                if count == len(needle):
                    return i-(count-1)
            else:
                count = 0
    return -1

print(indexOfFirstOccurance("aaaaa", "bba"))