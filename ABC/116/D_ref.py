N, K = [int(i) for i in input().split()]
tdList = [[int(i) for i in input().split()] for _ in range(N)]

type_sorted_tdList = sorted(tdList, key=lambda x: x[0], reverse=False)
sorted_tdList = sorted(tdList, key=lambda x: x[1], reverse=True)

iniSet = set()
for td in sorted_tdList:
    addFlag = False
    if not td[0] in iniSet:

    else:
        if count < K - type_sorted_tdList[-1][0]:
            addFlag = True
            typeDict[td[0]] += 1
            count += 1


