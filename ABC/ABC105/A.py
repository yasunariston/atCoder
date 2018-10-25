N, K = [int(i) for i in input().split()]
ans = 1

if N % K == 0:
    ans = 0

print(ans)
