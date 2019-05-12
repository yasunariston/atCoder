N, M = [int(i) for i in input().split()]
A = sorted([s for s in input().split()], reverse=True)
numDict = {"1":2, "2":5, "3":5, "4":4, "5":5, "6":6, "7":3, "8":7, "9":6}
dp = ["" for _ in range(N + 1)]

for i in range(N + 1):
    for strNum in A:
        if i - numDict[strNum] < 0:
            continue
        if i - numDict[strNum] == 0 and dp[i] == "":
            dp[i] = strNum
        preStrNum = dp[i - numDict[strNum]]
        if preStrNum != "":
            if len(preStrNum) + 1 > len(dp[i]):
                dp[i] = preStrNum + strNum

print("".join(sorted(dp[N], reverse=True)))
