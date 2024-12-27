def length(s):
    split = s.rstrip().split()
    return len(split[-1])

print(length("   fly me   to   the moon  "))
    
