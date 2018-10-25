N, L = [int(i) for i in input().split()]
sList = sorted([input() for _ in range(N)], key=lambda s: s)
s = ''.join(sList)
print(s)
