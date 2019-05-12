import numpy

N, K = [int(i) for i in input().split()]
S = input()

strList = [0, 0]
oneNum = 0
zeroNum = 0
if S[0] == "1":
    strList.append(0)

for i in range(N):
    if S[i] == "1":
        oneNum += 1
        if zeroNum != 0:
            strList.append(zeroNum)
        zeroNum = 0
    if S[i] == "0":
        zeroNum += 1
        if oneNum != 0:
            strList.append(oneNum)
        oneNum = 0

if oneNum != 0:
    strList.append(oneNum)
if zeroNum != 0:
    strList.append(zeroNum)

strList.append(0)
strList.append(0)

strCumsum = numpy.cumsum(strList).tolist()

ans = 0
for i, s in enumerate(strCumsum):
    if i % 2 == 1:
        ans = max(ans, strCumsum[i] - strCumsum[max(0, i - K * 2 - 1)])

print(ans)

