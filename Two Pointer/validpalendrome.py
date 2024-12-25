# def validpalendrome(s):
#     result = ''
#     for i in s.lower():
#         if (ord(i) >= 65 and ord(i)<=90) or (ord(i) >= 97 and ord(i)<=122) or (ord(i) >= 30 and ord(i)<=39):
#             result+=i
#     return result == result[::-1]
    


def validpalendrome(s):
    result = ''.join(c.lower() for c in s if c.isalnum())
    return result == result[::-1]

print(validpalendrome("A man, a plan, a canal: Panama"))
# import re

# def validpalendrome(s):
#     result = ''.join(re.findall(r'[a-zA-Z0-9]', s)).lower()
#     return result == result[::-1]



