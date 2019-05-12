N = int(input())
CList = [int(input()) for _ in range(N)]

CDict = {}
for i, C in enumerate(CList):
    if i == 0 or CList[i - 1] != C:
        if C in CDict:
            CDict[C] += 1
        else:
            CDict[C] = 1

ans = 1
for C in CDict:
    ans *= CDict[C]

ans -= 1

print(ans)
