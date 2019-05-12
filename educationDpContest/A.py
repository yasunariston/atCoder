N = int(input())
hList = [int(i) for i in input().split()]

dp = [float("inf") for _ in range(N)]
dp[0] = 0
dp[1] = abs(hList[1] - hList[0])
for i in range(2, N):
    dp[i] = min(dp[i - 1] + abs(hList[i] - hList[i - 1]), dp[i - 2] + abs(hList[i] - hList[i - 2]))

print(dp[N - 1])

