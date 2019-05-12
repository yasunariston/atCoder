L = int(input())
aList = []
for _ in range(L):
    aList.append(int(input()))

dp = [0 for _ in range(5)]
for a in aList:
    outer = a % 2 if a > 0 else 2
    inner = (a + 1) % 2
    dp[4] = min(dp[:5]) + a
    dp[3] = min(dp[:4]) + outer
    dp[2] = min(dp[:3]) + inner
    dp[1] = min(dp[:2]) + outer
    dp[0] += a

print(min(dp))

