def solve():
    N, W = map(int, input().split())

    dp = [0]  * (W + 1)
    items = []
    for i in range(N):
        w, v = map(int, input().split())
        items.append((w, v))

    for w, v in items:  
        for wk in range(W, w - 1, -1):
            tv = dp[wk - w] + v
            if tv > dp[wk]:
                dp[wk] = tv
        res = max(dp)
    print(res)

if __name__ == "__main__":
    solve()
