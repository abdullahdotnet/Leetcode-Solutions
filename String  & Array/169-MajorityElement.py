from collections import Counter


def majority(nums):
    counter = Counter(nums)
    return counter.most_common(1)[0][0]

print(majority([2,3,4,5,6,1,1,1,2,2,4,3,3]))