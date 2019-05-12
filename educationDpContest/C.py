N = int(input())
abcList = [[int(i) for i in input().split()] for _ in range(N)]

dp = [[0 for _ in range(3)] for _ in range(N)]
dp[0] = abcList[0]
for i in range(1, N):
    for j in range(3):
        for k, element in enumerate(abcList[i]):
            if j == k:
                continue
            dp[i][k] = max(dp[i - 1][j] + element, dp[i][k])

print(max(dp[N - 1]))

