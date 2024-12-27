def count_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    count = [0] * range_of_elements

    for num in arr:
        count[num - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    output = [0] * len(arr)
    for num in reversed(arr): 
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output


print(count_sort([2,1,3,4,5,0,2]))