import numpy as np

N, W = map(int, input().split())

dp = np.zeros(W + 1, dtype=int)
for i in range(N):
    w, v = map(int, input().split())
    print(dp[:W-w+1] + v)
    print(dp[w:])

    np.maximum(dp[:W-w+1]+v,dp[w:],out=dp[w:])
    print(dp)

print(dp[-1])

