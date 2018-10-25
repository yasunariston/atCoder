a = [int(i) for i in input().split()]
a1, a2, a3 = a[0], a[1], a[2]

ans = max(a1, a2, a3) - min(a1, a2, a3)
print(ans)
