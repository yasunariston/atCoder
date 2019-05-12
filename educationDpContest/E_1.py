import numpy as np

N, W = map(int, input().split())

dp = np.ones(N * 10 ** 3 + 1, dtype=int) * float("inf")
dp[0] = 0
for _ in range(N):
    w, v = map(int, input().split())
    np.minimum(dp[:v] + V)



