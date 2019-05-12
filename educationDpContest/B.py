N, K = list(map(int, input().split()))
hList = list(map(int, input().split()))

dp = [float("inf")] * N
dp[0] = 0
for i in range(N):
    for j in range(1, K + 1):
        if j > i:
            break
        dp[i] = min(dp[i - j] + abs(hList[i] - hList[i - j]), dp[i])

print(dp[N - 1])
