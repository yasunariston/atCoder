N, T = [int(i) for i in input().split()]
t = [int(i) for i in input().split()]
ans = T

for i in range(len(t) - 1):
    ans += min(T, t[i + 1] - t[i])

print(ans)

