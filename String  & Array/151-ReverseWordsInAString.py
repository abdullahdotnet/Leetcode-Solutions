def reverseWords(s):
    s = s.strip()
    s = s.split()
    res = " ".join(s[::-1])
    return res