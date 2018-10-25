ab = [int(i) for i in input().split()]
a, b = ab[0], ab[1]

dif = b - a
ans = int((1 + dif) * dif / 2 - b)
print(ans)
