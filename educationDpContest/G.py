from collections import defaultdict

N, M = map(int, input().split())
graphDict = defaultdict(list)
for _ in range(M):
    x, y = map(int, input().split())
    graphDict[x].append(y)


print(graphDict)


"""

// 1

1 -> 2 = 2

n1を起点とする最大値
n2を終点とする最大値


1 2
1 -> 2

1 3
1 -> 2
1 -> 3

2 3
1 -> 2
1 -> 2 -> 3

2 4
1 -> 2
1 -> 2 -> 3
1 -> 2 -> 4

4 5
1 -> 2
1 -> 2 -> 3
1 -> 2 -> 4 -> 5

6 7
1 -> 2
1 -> 2 -> 3
1 -> 2 -> 4
1 -> 2 -> 4 -> 5
6 -> 7

3 6



"""
