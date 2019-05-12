import numpy as np

A, B, Q = [int(i) for i in input().split()]
sList = np.asarray([int(input()) for _ in range(A)])
tList = np.asarray([int(input()) for _ in range(B)])
xList = np.asarray([int(input()) for _ in range(Q)])

def getDist(distance, someList):
    idx = np.abs(someList - distance).argmin()
    return [someList[max(idx - 1, 0)], someList[idx], someList[min(idx + 1, len(someList) - 1)]]

for x in xList:
    sDists = getDist(x, sList)
    tDists = getDist(x, tList)
    ans = float("inf")
    for s in sDists:
        for t in tDists:
            ans = min(ans, min(abs(x - s), abs(x - t)) + abs(s - t))
    print(ans)

