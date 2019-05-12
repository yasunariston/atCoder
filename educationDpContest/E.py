N, W = map(int, input().split())

dp = [[float("inf")] * (N * 10 ** 3 + 1) for _ in range(2)]
dp[0][0], dp[1][0] = 0, 0
for i in range(N):
    index = i % 2
    w, v = map(int, input().split())
    for j in range(1, len(dp[0])):
        if j <= v:
            dp[index][j] = min(w, dp[index-1][j])
        else:
            dp[index][j] = min(w + dp[index-1][j-v], dp[index-1][j])

ans = 0
for i, w in enumerate(dp[N % 2 - 1]):
    if w <= W:
        ans = max(ans, i)
    else:
        break

print(ans)
