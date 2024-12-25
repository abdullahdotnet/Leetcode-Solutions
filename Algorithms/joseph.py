def josephus(n, k):
    return 0 if n == 0 else (josephus(n - 1, k) + k) % n


print(josephus(41, 3))