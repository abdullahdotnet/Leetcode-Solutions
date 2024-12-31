def reverseWords(s):
    s = s.strip()
    s = s.split()
    res = " ".join(s[::-1])
    return res

# def reverseWords(s):
#     words = s.split()
#     left, right = 0, len(words) - 1

#     while left < right:
#         words[left], words[right] = words[right], words[left]
#         left += 1
#         right -= 1

#     return " ".join(words) 


# def reverseWords(s):
#     words = s.split()
#     res = []

#     for i in range(len(words) - 1, -1, -1):
#         res.append(words[i])
#         if i != 0:
#             res.append(" ")

#     return "".join(res)