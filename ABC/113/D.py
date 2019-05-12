import math

H, W, K = [int(i) for i in input().split()]
dp = [[0 for _ in range(W)] for _ in range(H)]
dp[0][0] = 1

startBit = "0b" + "0" * W
endBit = "0b" + "1" * W
counta = 0

print(startBit)

