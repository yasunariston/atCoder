import time

N, M = [int(i) for i in input().split()]
A = sorted([s for s in input().split()], reverse=True)
numDict = {"1":2, "2":5, "3":5, "4":4, "5":5, "6":6, "7":3, "8":7, "9":6}

start = time.time()
dp = [0 for _ in range(N + 1)]
count = 0
for i in range(N + 1):
    for strNum in A:
        if i - numDict[strNum] == 0:
            dp[i] = max(dp[i], int(strNum))
            continue
        if dp[i - numDict[strNum]] != 0:
            dp[i] = max(dp[i], int(str(dp[i - numDict[strNum]]) + strNum))

print(dp[N])

elapsed_time = time.time() - start
print(elapsed_time)
