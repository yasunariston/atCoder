import numpy as np
from collections import defaultdict as dd

X, Y, Z, K = [int(i) for i in input().split()]
ABCLists = [np.array([int(i) for i in input().split()]) for _ in range(3)]

for i in range(len(ABCLists)):
    ABCLists[i] = np.sort(ABCLists[i])[::-1]
    ABCLists[i] = ABCLists[i][0] - ABCLists[i]

abci = [0, 0, 0]
dpDict = dd(int)
dpDict[0] = 1
while(True):
    if abci == [X - 1, Y - 1, Z - 1]:
        break
    min_i = 0
    min_diff = np.inf
    for i, ABCList in enumerate(ABCLists):
        if abci[i] < len(ABCList):
            min_diff = ABCList[abci[i] + 1]
            min_i = i
    abci[min_i] += 1
    keys = list(dpDict.keys()).copy()
    for key in keys:
        dpDict[min_diff + key] += 1

print(dpDict)
















print(ABCLists)







