import math

N, K = [int(i) for i in input().split()]

ans = "YES"
if math.ceil(N / 2)< K:
    ans = "NO"

print(ans)
