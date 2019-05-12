import math

N, K = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]

bitDict = {}
count = 0
while(True):
    if K >= int(math.pow(2, count)):
        bitDict[count] = 0
    else:
        break
    count += 1

ans = 0
for a in A:
    a = bin(a)
    for i, s in enumerate(str(a)[2:][::-1]):
        if i in bitDict:
            bitDict[i] += int(s)
        else:
            ans += int(math.pow(2, i)) * int(s)

bitList = [0 if bitDict[i] >= N - bitDict[i] else 1 for i in bitDict]
for i, bit in enumerate(bitList):
    if bit == 0:
    ans += int(math.pow(2, i)) * bitDict[i]
        continue




