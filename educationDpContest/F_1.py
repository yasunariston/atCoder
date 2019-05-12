sList, tList = list(input()), list(input())

dp = [[0] * (len(tList) + 1) for _ in range(len(sList) + 1)]
for i, s in enumerate(sList, start=1):
    sameNum = 0
    for j, t in enumerate(tList, start=1):
        num = dp[i-1][j]
        if s == t:
            sameNum = max(num, dp[i-1][j-1] + 1)
        dp[i][j] = max(num, sameNum)

ans = ""

while(i > 0, j > 0):
    num = dp[i][j]
    if num == 0:
        break
    if sList[i-1] == tList[j-1]:
        ans = sList[i-1] + ans
        i -= 1
        j -= 1
    else:
        if dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

print(ans)

"""
axyb
abyxb

# 0 1 2 3 4 5
0 0 0 0 0 0 0
1 0 1 1 1 1 1
2 0 1 1 1 2 2
3 0 1 1 2 2 2
4 0 1 2 2 2 3


"""
