from collections import defaultdict

N = int(input())
abList = [list(map(int, input().split())) for _ in range(N-1)]

treeDict = defaultdict(list)
for ab in abList:
    a, b = ab
    treeDict[a].append(b)
    treeDict[b].append(a)

costDict = defaultdict(int)
treeQ = set()
for i in range(1, N + 1):
    if len(treeDict[i]) == 1:
        costDict[i] = 1
        treeQ.add(treeDict[i][0])

treeMaxLen = 0
continueFlg = True
while(continueFlg):
    tQ = set()
    for i, n1 in enumerate(treeQ):
        decidedFlg = True
        cost = -1
        qTemp = -1
        for j, n2 in enumerate(treeDict[n1]):
            if costDict[n2] == 0:
                if not decidedFlg:
                    cost = -1
                    qTemp = -1
                    break
                qTemp = n2
                decidedFlg = False
            else:
                cost = max(cost, costDict[n2] + 1)

        if decidedFlg:
            firstLen, secondLen = -1, -1
            for i, n2 in enumerate(costDict):
                if costDict[n2] > firstLen:
                    secondLen = firstLen
                    firstLen = costDict[n2]
                elif costDict[n2] > secondLen:
                    secondLen = costDict[n2]
            treeMaxLen = firstLen + secondLen + 1
            continueFlg = False
            break

        if cost != -1:
            costDict[n1] = cost
            tQ.add(qTemp)
    treeQ = tQ

ans = "First" if treeMaxLen % 3 != 2 else "Second"
print(ans)

