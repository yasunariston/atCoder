import math

NC = [int(i) for i in input().split()]
N, C = NC[0], NC[1]
strange = [[int(i) for i in input().split()] for _ in range(C)]
grid = []
for i in range(N):
    grid.extend([int(i) for i in input().split()])

amount = int(math.pow(N, 2))
countaList = [{} for _ in range(3)]
pointList = [{} for _ in range(3)]

for step in range(3):
    for i in range(step, amount, 3):
        if grid[i] in countaList[step]:
            countaList[step][grid[i]] += 1
        else:
            countaList[step][grid[i]] = 1

for step in range(3):
    counta = countaList[step]
    point = pointList[step]
    stepAmount = int(math.round((amount - step) / 3))
    for i in counta:
        point[i] = (stepAmount - counta[i]) *





print(countaList)
