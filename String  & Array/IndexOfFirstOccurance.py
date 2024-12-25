def indexOfFirstOccurance(heystack,needle):
    i = 0
    j = 0
    count = 0
    while i < len(heystack) and j < len(needle):
        if heystack[i] == needle[j]:
            count+=1
            if count == len(needle):
                return (i+1)-(count)
            i+=1
            j+=1
        elif heystack[i] != needle[j]:
            if count == 0:
                i+=1
            else:
                j-=count
                i-=count-1
                count = 0
                
    return -1

print(indexOfFirstOccurance("mississippi", "issip"))