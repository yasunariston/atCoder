import math

N, M, q = [int(i) for i in input().split()]
xpList = [[int(i) for i in input().split()] for _ in range(N)]

p_half = 0
firstHalfEnd_index = M - 2
for i, xp in enumerate(xpList):
    p_half += xp[1]
    if p_half >= q // 2:
        firstHalfEnd_index = i
        break

print(firstHalfEnd_index)
sum_firstHalf = sum([xp[0] for i, xp in enumerate(xpList) if i < firstHalfEnd_index])
sum_firstHalfEnd = sum([xp[0] for i, xp in enumerate(xpList) if i >= firstHalfEnd_index])

ans = math.pow(10, 10)
for i in range(xpList[firstHalfEnd_index][0], xpList[firstHalfEnd_index+1][0]):
    dis = 0
    for xp in xpList:
        dis += abs(xp[0] - i) * (xp[1] / q)
    ans = min(ans, dis)

print(ans)


'''

1 3 100
1 30
3 20
9 50

|x - 1| * 0.3 =
|x - 3| * 0.2 =
|x - 9| * 0.5 =

x = 6 -> 1.5 + 0.6 + 1.5 = 3.6
x = 7 -> 1.8 + 0.8 + 1.0 = 3.6


2 3 100
1 30
3 20
9 50

|x - 1| * 0.3 =
|x - 3| * 0.2 =
|x - 9| * 0.5 =

'''
