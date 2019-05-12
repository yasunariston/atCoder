import heapq
from collections import defaultdict as dd

X, Y, Z, K = [int(i) for i in input().split()]
ABCList = [sorted([int(i) for i in input().split()], reverse=True) for _ in range(3)]

pQ = []
heapq.heappush(pQ, [sum(ABC[0] for ABC in ABCList) * (-1), [0, 0, 0]])
QDict = dd(int)
QDict[(0, 0, 0)] = 1
for _ in range(K):
    item = heapq.heappop(pQ)
    print(item[0] * (-1))
    abc = item.copy()[1]
    for i, element in enumerate(abc):
        abcTemp = abc.copy()
        abcTemp[i] += 1
        if abcTemp[i] < len(ABCList[i]) and QDict[tuple(abcTemp)] == 0:
            newItem = [sum([ABCList[i][abcTemp[i]] for i in range(3)]) * (-1), abcTemp]
            heapq.heappush(pQ, newItem)
            QDict[(tuple(abcTemp))] = 1

