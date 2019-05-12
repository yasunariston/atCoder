import numpy as np

N, K = [int(i) for i in input().split()]
a = np.cumsum([int(i) for i in input().split()])
a = np.insert(a, 0, 0)

numList = []
for i in range(0, N):
    for j in range(i+1, N+1):
        numList.append(a[j] - a[i])

numList = sorted(numList, reverse=True)
t

print(numList)
