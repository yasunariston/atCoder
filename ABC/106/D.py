N, M, Q = [int(i) for i in input().split()]

trainTable = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    l, r = [int(i) - 1 for i in input().split()]
    trainTable[l][r] += 1

for trainList in trainTable:
    for i in trainList:
        if i != 0:
            trainList[i] += trainList[i - 1]

print(trainTable)

for i in range(M):
    input()


'''
TLE

N, M, Q = [int(i) for i in input().split()]
trainDict = {}
for _ in range(M):
    l, r = [int(i) for i in input().split()]
    if l in trainDict:
        trainDict[l].append(r)
    else:
        trainDict[l] = [r]

keys = sorted(trainDict.keys())
for _ in range(Q):
    p, q = [int(i) for i in input().split()]
    ans = 0
    for key in keys:
        if key > q:
            break
        if key >= p:
            ans += len([i for i in trainDict[key] if i <= q])
    print(ans)
'''

