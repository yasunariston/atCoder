import math

N, K = [int(i) for i in input().split()]
tdList = [[int(i) for i in input().split()] for _ in range(N)]

type_sorted_tdList = sorted(tdList, key=lambda x: x[0], reverse=False)
sorted_tdList = sorted(tdList, key=lambda x: x[1], reverse=True)

ans = 0
iniList = []
typeDict = {}
count = 0
for i, td in enumerate(sorted_tdList):
    addFlag = False
    if td[0] not in typeDict:
        addFlag = True
        typeDict[td[0]] = 1
    else:
        if count < K - type_sorted_tdList[-1][0]:
            addFlag = True
            typeDict[td[0]] += 1
            count += 1
    if addFlag:
        ans += td[1]
        iniList.append(td)
        rmTd = sorted_tdList.pop(i)
        sorted_tdList.insert(0, rmTd)
    if len(iniList) == K:
        break

ans += math.pow(2, len(typeDict))
del sorted_tdList[:K]

for td in iniList[::-1]:
    diff = 0
    typeDict[td[0]] -= 1
    if typeDict[td[0]] == 0:
        typeDict.pop(td[0])
        diff -= math.pow(2, (len(typeDict) + 1)) - math.pow(2, len(typeDict))
    diff -= td[1]
    if len(sorted_tdList) > 0:
        diff += sorted_tdList[0][1]
        sorted_tdList.pop(0)
    if diff > 0:
        ans += diff
    else:
        break

print(int(ans))
