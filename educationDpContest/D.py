N, W = list(map(int, input().split()))
wvList = [map(int, input().split()) for _ in range(N)]

DP = [0] * (W + 1)
for w, v in wvList:
    for rj in range(W, w - 1, -1):
        num = DP[rj - w] + v
        if num > DP[rj]:
            DP[rj] = num

print(max(DP))
