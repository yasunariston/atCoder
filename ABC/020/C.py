from collections import defaultdict

H, W, T = map(int, input().split())
field = [input() for _ in range(H)]


def dikstra(H, W, field):
    costDict = defaultdict(float("inf"))
    for i, wList in enumerate(field):
        for j, element in enumerate(wList):
            if i > 0:
                costDict[(i-1, j)] = min(costDict[(i-1, j)], costDict[(i, j)] + leftCost)
            if i < W - 1:
                costDict[(i+1, j)] = min(costDict[(i+1, j)], costDict[(i, j)] + rightCost)
            if j > 0:
                









print(field)
