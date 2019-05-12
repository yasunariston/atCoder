NM = [int(i) for i in input().split()]
p = [int(i) for i in input().split()]
xyList = [frozenset([int(i) for i in input().split()]) for _ in range(NM[1])]
contFlag = True

while(contFlag):
    contFlag = False
    for i in range(len(xyList)):
        for j in range(len(xyList)):
            if len(xyList[i] & xyList[j]) != 0:
                xyList[i] |= xyList[j]
                xyList[j] |= xyList[i]
                if not xyList[i] <= xyList[j] and not xyList[i] >= xyList[j]:
                    contFlag = True

xySet = set(xyList)
ans = 0
for xy in xySet:
    for num in p:
        if not num in xy:
