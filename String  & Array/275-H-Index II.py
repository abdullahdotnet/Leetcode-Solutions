def hIndex(citations):
    h_index = 0
    left, right = 0, len(citations) - 1
    i = 0
    while left <= right:
        minNoOfCitations = len(citations) - i
        mid = left + (right - left) // 2
        if citations[mid] == minNoOfCitations:
            return minNoOfCitations
        elif citations[mid] < minNoOfCitations:
            left = mid + 1
        else:
            right = mid - 1
    return h_index

print(hIndex([3,0,6,1,5]))