NM = [int(i) for i in input().split()]
N, M = NM[0], NM[1]
abList = sorted([[int(i) for i in input().split()] for _ in range(M)], key=lambda x: x[1])
bridge = 0
ans = 0

for ab in abList:
    if not ab[0] <= bridge < ab[1]:
        bridge = ab[1] - 1
        ans += 1

print(ans)


'''
#TLE

NM = [int(i) for i in input().split()]
N, M = NM[0], NM[1]
ans = 0

while(True):
    bridgeDic = {}
    for ab in abList:
        if ab != None:
            for i in range(ab[0], ab[1]):
                if i in bridgeDic:
                    bridgeDic[i] += 1
                else:
                    bridgeDic[i] = 1

    largeNum = 0
    largeKey = 0
    for i in bridgeDic:
        if bridgeDic[i] > largeNum:
            largeNum = bridgeDic[i]
            largeKey = i

    ans += 1
    M -= bridgeDic[largeKey]
    if M <= 0:
        break

    for i in range(len(abList)):
        if abList[i] != None and abList[i][0] <= largeKey < abList[i][1]:
            abList[i] = None

print(ans)
'''

